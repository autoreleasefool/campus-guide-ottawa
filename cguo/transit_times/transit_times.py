"""Transit data caching and parsing."""
# pylint:disable=W0703

import argparse
from datetime import datetime
import io
import json
import re
import os
import zipfile
import shutil
import sys
import pytz
import requests


def get_cache_dir():
    """Get the directory of the cache."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'temp_data')


def get_config_dir():
    """Get the directory of the config."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'json')


def update_data():
    """Updated OC Transpo data cache."""
    print('Downloading data')
    zip_url = 'http://www.octranspo1.com/files/google_transit.zip'

    response = requests.get(zip_url, timeout=10)
    if response.status_code != 200:
        print('Download of data failed.')
        sys.exit(1)

    zipped_transit_data = zipfile.ZipFile(io.BytesIO(response.content))
    zipped_transit_data.extractall(path=os.path.join(get_cache_dir(), 'txt'))


def get_value_index_from_dict_array(key, value, array):
    """Checks if a key value pair appears anywhere in an array of dicts."""
    for i, dic in enumerate(array):
        if dic[key] == value:
            return i
    return -1


def import_city_transit():
    """Import city transit data from config."""
    print('Read', os.path.join(get_config_dir(), 'city_transit.json'))
    output = {}
    with open(os.path.join(get_config_dir(), 'city_transit.json'), encoding='utf8') as ctf:
        city_transit_json = json.loads(ctf.read())
        for key in city_transit_json:
            output[key] = city_transit_json[key]
    return output


def import_campuses_and_stops():
    """Import transit campuses and stops from config."""
    campuses = {}
    campus_stops = {}
    print('Read', os.path.join(get_config_dir(), 'stops.json'))
    with open(os.path.join(get_config_dir(), 'stops.json'), encoding='utf8') as campus_stops_file:
        stop_json = json.loads(campus_stops_file.read())
        for campus in stop_json:
            campuses[campus] = {
                'id': campus,
                'name_en': stop_json[campus]['name_en'],
                'name_fr': stop_json[campus]['name_fr'],
                'lat': stop_json[campus]['lat'],
                'long': stop_json[campus]['long'],
                'stops': {},
            }

            for stop in stop_json[campus]['stops']:
                campus_stops[stop] = campus
    return campuses, campus_stops


def parse_stops(campus_stops):
    """Parse stop data from OC Transpo."""
    print('Parse', os.path.join(get_cache_dir(), 'txt', 'stops.txt'))
    output = {'stopDetails': {}}
    with open(os.path.join(get_cache_dir(), 'txt', 'stops.txt'), encoding='utf8') as stop_file:
        for stop in stop_file:
            if 'stop_id' in stop:
                continue
            stop_info = re.match(r'(.*?),(.*?),(.*?),.*?,([\d.-]+),([\d.-]+),', stop)
            stop_code = stop_info.group(2)

            if stop_code in campus_stops:
                stop_id = stop_info.group(1)
                stop_name = stop_info.group(3)
                stop_latitude = stop_info.group(4)
                stop_longitude = stop_info.group(5)

                # Make stop names more consistent
                stop_name = stop_name.replace('\\', '/').replace('"', '')

                output['stopDetails'][stop_id] = {
                    'campus': campus_stops[stop_code],
                    'code': stop_code,
                    'name': stop_name,
                    'lat': float(stop_latitude),
                    'long': float(stop_longitude),
                }
    return output


def parse_calendar():
    """Parse OC Transpo service calendar."""
    print('Parse', os.path.join(get_cache_dir(), 'txt', 'calendar.txt'))
    valid_services = {}
    with open(os.path.join(get_cache_dir(), 'txt', 'calendar.txt'), encoding='utf8') as cal_file:
        for service in cal_file:
            if 'service_id' in service:
                continue
            service_info = re.match(r'(.*?),(\d),(\d),(\d),(\d),(\d),(\d),(\d),(.*?),(.*?)$',
                                    service)
            service_id = service_info.group(1)
            service_start_date = service_info.group(9)
            service_end_date = service_info.group(10)

            service_start = datetime.strptime(service_start_date, '%Y%m%d')
            service_end = datetime.strptime(service_end_date, '%Y%m%d')
            today = datetime.today()

            timezone = pytz.timezone("Canada/Eastern")
            service_start = timezone.localize(service_start)
            service_end = timezone.localize(service_end)
            today = timezone.localize(today)

            if today >= service_start and today <= service_end:
                valid_services[service_id] = []
                for i in range(2, 9):
                    if service_info.group(i) == '1':
                        valid_services[service_id].append(str(i - 2))
    return valid_services


def parse_trips(valid_services):
    """Parse trip information from OC Transpo."""
    valid_trips = {}
    print('Parse', os.path.join(get_cache_dir(), 'txt', 'trips.txt'))
    with open(os.path.join(get_cache_dir(), 'txt', 'trips.txt'), encoding='utf8') as trips_file:
        for trip in trips_file:
            if 'route_id' in trip:
                continue
            trip_info = re.match(r'(.*?),(.*?),(.*?),(.*?),(.*?),', trip)
            service_id = trip_info.group(2)

            if service_id in valid_services:
                route_id = trip_info.group(1)
                trip_id = trip_info.group(3)
                trip_headsign = trip_info.group(4)
                direction = trip_info.group(5)

                valid_trips[trip_id] = {
                    'route': int(route_id[:route_id.index('-')]),
                    'headsign': trip_headsign.replace('"', ''),
                    'direction': direction,
                    'days': valid_services[service_id],
                }
    return valid_trips


def parse_stop_times(campuses, valid_trips, output):
    """Parse route stop times at valid stops."""
    print('Parse', os.path.join(get_cache_dir(), 'txt', 'stop_times.txt'))
    with open(os.path.join(get_cache_dir(), 'txt', 'stop_times.txt'), encoding='utf8') as stf:
        for stop in stf:
            if 'trip_id' in stop:
                continue
            stop_info = re.match(r'(.*?),(.*?),.*?,(.*?),', stop)
            tid = stop_info.group(1)
            sid = stop_info.group(3)

            if sid in output['stopDetails'] and tid in valid_trips:
                arrival = stop_info.group(2)
                route_id = valid_trips[tid]['route']
                campus = output['stopDetails'][sid]['campus']
                cidx = get_value_index_from_dict_array('id', campus, output['campuses'])
                if cidx == -1:
                    output['campuses'].append(campuses[campus])
                    cidx = len(output['campuses']) - 1
                if sid not in output['campuses'][cidx]['stops']:
                    output['campuses'][cidx]['stops'][sid] = []

                ridx = get_value_index_from_dict_array(
                    'number',
                    route_id,
                    output['campuses'][cidx]['stops'][sid]
                )

                if ridx == -1:
                    output['campuses'][cidx]['stops'][sid].append({
                        'number': route_id,
                        'sign': valid_trips[tid]['headsign'],
                    })
                if 'days' not in output['campuses'][cidx]['stops'][sid][ridx]:
                    output['campuses'][cidx]['stops'][sid][ridx]['days'] = {}
                for i in valid_trips[tid]['days']:
                    if i not in output['campuses'][cidx]['stops'][sid][ridx]['days']:
                        output['campuses'][cidx]['stops'][sid][ridx]['days'][i] = []
                    output['campuses'][cidx]['stops'][sid][ridx]['days'][i].append(arrival[0:5])


def compact_data(output):
    """Compact data."""
    # pylint:disable=C0301,R1702
    print('Compacting data')
    for stop_id in output['stopDetails']:
        del output['stopDetails'][stop_id]['campus']

    for campus_index in range(len(output['campuses'])):
        for stop_id in output['campuses'][campus_index]['stops']:
            for route_index in range(len(output['campuses'][campus_index]['stops'][stop_id])):
                days_and_times = {}
                for day, times in output['campuses'][campus_index]['stops'][stop_id][route_index]['days'].items():
                    if times not in days_and_times.values():
                        days_and_times[day] = times
                    else:
                        for i in days_and_times:
                            if days_and_times[i] == times:
                                days_and_times[str(i) + str(day)] = times
                                del days_and_times[i]
                                break
                output['campuses'][campus_index]['stops'][stop_id][route_index]['days'] = {}
                for key in days_and_times:
                    sorted_key = ''.join(sorted(key))
                    output['campuses'][campus_index]['stops'][stop_id][route_index]['days'][sorted_key] = days_and_times[key]
                    output['campuses'][campus_index]['stops'][stop_id][route_index]['days'][sorted_key] = sorted(output['campuses'][campus_index]['stops'][stop_id][route_index]['days'][sorted_key])


def write_data(output, dest, pretty):
    """Output data to file dest."""
    with open(dest, 'w', encoding='utf8') as outfile:
        if pretty:
            json.dump(output, outfile, indent=2, sort_keys=True, ensure_ascii=False)
        else:
            json.dump(output, outfile, sort_keys=True, ensure_ascii=False)


def parse_data(dest, pretty):
    """Parse OC Transpo data."""
    output = {
        'stopDetails': {},
        'campuses': [],
    }

    campuses, campus_stops = import_campuses_and_stops()
    output = {**output, **import_city_transit()}
    output = {**output, **parse_stops(campus_stops)}
    valid_services = parse_calendar()
    valid_trips = parse_trips(valid_services)
    parse_stop_times(campuses, valid_trips, output)
    compact_data(output)
    write_data(output, dest, pretty)


def parse_transit_times(args, dest):
    """Parse OC Transpo transit times."""
    if args is None:
        args = []

    arg_parser = argparse.ArgumentParser(description='OC Transpo transit parsing')
    arg_parser.add_argument('-u', '--update-cache',
                            action='store_true',
                            help='''Download the OC Transpo data from the web and override
                                    the current data before parsing the data''')
    arg_parser.add_argument('-p', '--pretty',
                            action='store_true',
                            help='Indent JSON output')
    arg_parser.add_argument('-c', '--clean',
                            action='store_true',
                            help='clean up cached data after')
    parsed_args = arg_parser.parse_args(args)

    if parsed_args.update_cache:
        update_data()

    try:
        with open(os.path.join(get_cache_dir(), 'txt', 'stops.txt')):
            print('Bus data exists. Continuing.')
    except Exception:
        print('Could not find bus data. Downloading.')
        update_data()

    parse_data(dest, parsed_args.pretty)
    if parsed_args.clean:
        print('Cleaning up')
        shutil.rmtree(get_cache_dir())
