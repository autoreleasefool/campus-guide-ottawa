#
# Transit Data
#

# Options:
#
#    --update-info, -u
#        Downloads the OC Transpo data from the web and overrides the current data
#        before parsing the data
#
#    --pretty
#        If included, JSON output will be indented

import io
import os
import requests
import sys
import zipfile

def updateData():
  print('Downloading data')
  zip_url = 'http://www.octranspo1.com/files/google_transit.zip'

  response = requests.get(zip_url)
  if response.status_code != 200:
    sys.exit(0)

  zipped_transit_data = zipfile.ZipFile(io.BytesIO(response.content))
  zipped_transit_data.extractall(path='temp_data/txt');

if '--update-info' in sys.argv or '-u' in sys.argv:
  updateData()

# Parsing

import datetime
import json
import re
import sys

campuses = {}
campus_stops = {}
stops = {}
valid_services = {}
valid_trips = {}
output = {
  'stop_details': {},
  'campuses': []
}

# Checks if a key value pair appears anywhere in an array of dicts
def get_key_value_index_in_array_of_dicts(key, value, array):
  for i in range(len(array)):
    if array[i][key] == value:
      return i
  return -1

print('Open json/city_transit.json')
with open('json/city_transit.json') as city_transit_file:
  city_transit_json = json.loads(city_transit_file.read())
  for key in city_transit_json:
    output[key] = city_transit_json[key]

print('Open json/stops.json')
with open('json/stops.json') as campus_stops_file:
  stop_json = json.loads(campus_stops_file.read())
  for campus in stop_json:
    campuses[campus] = {
      'id': campus,
      'name_en': stop_json[campus]['name_en'],
      'name_fr': stop_json[campus]['name_fr'],
      'lat': stop_json[campus]['lat'],
      'long': stop_json[campus]['long'],
      'stops': {}
    }

    for stop in stop_json[campus]['stops']:
      campus_stops[stop] = campus

try:
  with open('temp_data/txt/stops.txt') as temp:
    print('Bus data exists. Continuing.')
except Exception as error:
  print('Could not find bus data. Downloading.')
  updateData()

print('Open temp_data/txt/stops.txt')
with open('temp_data/txt/stops.txt') as stop_file:
  for stop in stop_file:
    if 'stop_id' in stop: continue
    stop_info = re.match(r'(.*?),(.*?),(.*?),.*?,([\d.-]+),([\d.-]+),', stop)
    stop_code = stop_info.group(2)

    if stop_code in campus_stops:
      stop_id = stop_info.group(1)
      stop_name = stop_info.group(3)
      stop_latitude = stop_info.group(4)
      stop_longitude = stop_info.group(5)

      # Make stop names more consistent
      stop_name = stop_name.replace('\\', '/').replace('"', '')

      output['stop_details'][stop_id] = {
        'campus': campus_stops[stop_code],
        'code': stop_code,
        'name': stop_name,
        'lat': float(stop_latitude),
        'long': float(stop_longitude)
      }

print('Open temp_data/txt/calendar.txt')
with open('temp_data/txt/calendar.txt') as calendar_file:
  for service in calendar_file:
    if 'service_id' in service: continue
    service_info = re.match(r'(.*?),(\d),(\d),(\d),(\d),(\d),(\d),(\d),(.*?),(.*?)$', service)
    service_id = service_info.group(1)
    service_start_date = service_info.group(9)
    service_end_date = service_info.group(10)

    service_start_month = int(service_start_date[4:6])
    service_start_day = int(service_start_date[6:])
    service_end_month = int(service_end_date[4:6])
    service_end_day = int(service_end_date[6:])

    current_month = datetime.date.today().month
    current_day = datetime.date.today().day

    if (current_month > service_start_month or (current_month == service_start_month and current_day >= service_start_day)) and (current_month < service_end_month or (current_month == service_end_month and current_day <= service_end_day)):
      valid_services[service_id] = []
      for i in range(2, 9):
        if (service_info.group(i) == '1'): valid_services[service_id].append(str(i - 2))

print('Open temp_data/txt/trips.txt')
with open('temp_data/txt/trips.txt', encoding='utf8') as trips_file:
  for trip in trips_file:
    if 'route_id' in trip: continue
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
        'days': valid_services[service_id]
      }

print('Open temp_data/txt/stop_times.txt')
with open('temp_data/txt/stop_times.txt') as stop_times_file:
  for stop in stop_times_file:
    if 'trip_id' in stop: continue
    stop_info = re.match(r'(.*?),(.*?),.*?,(.*?),', stop)
    trip_id = stop_info.group(1)
    stop_id = stop_info.group(3)

    if stop_id in output['stop_details'] and trip_id in valid_trips:
      arrival_time = stop_info.group(2)
      route_id = valid_trips[trip_id]['route']
      campus = output['stop_details'][stop_id]['campus']
      campus_index = get_key_value_index_in_array_of_dicts('id', campus, output['campuses'])
      if campus_index == -1:
        output['campuses'].append(campuses[campus])
        campus_index = len(output['campuses']) - 1
      if stop_id not in output['campuses'][campus_index]['stops']:
        output['campuses'][campus_index]['stops'][stop_id] = []
        # output['stop_details'][stop_id] = {
        #   'code': output['stop_details'][stop_id]['code'],
        #   'name': output['stop_details'][stop_id]['name'],
        #   'lat': output['stop_details'][stop_id]['lat'],
        #   'long': output['stop_details'][stop_id]['long']
        # }

      route_index = get_key_value_index_in_array_of_dicts('number', route_id, output['campuses'][campus_index]['stops'][stop_id])
      if route_index == -1:
        output['campuses'][campus_index]['stops'][stop_id].append({
          'number': route_id,
          'sign': valid_trips[trip_id]['headsign']
        })
      if 'days' not in output['campuses'][campus_index]['stops'][stop_id][route_index]:
        output['campuses'][campus_index]['stops'][stop_id][route_index]['days'] = {}
      for i in valid_trips[trip_id]['days']:
        if i not in output['campuses'][campus_index]['stops'][stop_id][route_index]['days']:
          output['campuses'][campus_index]['stops'][stop_id][route_index]['days'][i] = []
        output['campuses'][campus_index]['stops'][stop_id][route_index]['days'][i].append(arrival_time[0:5])

# Compacting data
print('Compacting data')
for stop_id in output['stop_details']:
  del output['stop_details'][stop_id]['campus']

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

# Output
if not os.path.exists('../output'):
  os.mkdir('./output')
with open('./output/bus.json', 'w', encoding='utf8') as outfile:
  if '--pretty' in sys.argv:
    json.dump(output, outfile, indent=2, sort_keys=True, ensure_ascii=False)
  else:
    json.dump(output, outfile, sort_keys=True, ensure_ascii=False)
