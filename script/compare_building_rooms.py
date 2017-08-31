#!/usr/bin/env python3

"""
Compare rooms identified by assets_server/text/*_graph.txt to those in assets_app/js/Building.js
and list rooms which appear in one, but not the other.
"""

# pylint:disable=C0103

import os
import re
import sys

if len(sys.argv) < 2:
    print('\nUse this tool to ensure buildings rooms have all been accounted for.')
    print('Usage: ./script/compare_building_rooms.py <building_code>')
    exit()

building_shorthand = sys.argv[1]

def load_files():
    """
    Loads rooms from relevant files and returns two sets, or None in place of a set for a file
    which could not be opened.

    :rtype:
        `set` or None, `set` or None
    """
    json_room_listing = None
    graph_room_listing = None
    print('Parsing Buildings.js')
    with open(os.path.join('assets_app', 'js', 'Buildings.js')) as building_file:
        json_room_listing = set()
        line = building_file.readline()
        collect_rooms = False
        last_name = ''
        while line:
            name_pos = line.find(' name:')
            if name_pos > 0 and collect_rooms:
                room_name = line[name_pos + 8:line.find('\'', name_pos + 8)]
                if room_name in json_room_listing:
                    print('  Duplicate name found! `{0}`'.format(room_name))
                if room_name < last_name:
                    print('  Room out of order! `{0}`'.format(room_name))
                json_room_listing.add('R{0}'.format(room_name))
                last_name = room_name
            elif 'shorthand' in line:
                shorthand = line[line.find('shorthand') + 12:line.rfind('\'')]
                if shorthand == building_shorthand:
                    collect_rooms = True
                elif collect_rooms:
                    break
            line = building_file.readline()

    print('Parsing {0}_graph.txt'.format(building_shorthand))
    with open(os.path.join(
        'assets_server',
        'text',
        '{0}_graph.txt'.format(building_shorthand)
        )) as graph_file:
        graph_room_listing = set()
        line = graph_file.readline()
        while line:
            if re.match(r'^(R[\d\w]+)[|].*', line):
                room_name = line[:line.find('|')]
                if room_name in graph_room_listing:
                    print('  Duplicate name found! `{0}`'.format(room_name))
                graph_room_listing.add(room_name)
            line = graph_file.readline()

    return json_room_listing, graph_room_listing

def print_missing_rooms(rooms):
    """
    Print a list of missing rooms in alphanumeric order.

    :param rooms:
        Set of room names
    :type rooms:
        `set`
    """
    if not rooms:
        print('\tNone!')
        return
    room_names = [x for x in rooms]
    room_names.sort()
    for room_name in room_names:
        print('  {', end='')
        print(' name: \'{0}\' '.format(room_name[1:]), end='')
        print('},')

print()
building_rooms, graph_rooms = load_files()
if building_rooms is None:
    print('Could not find assets_app/js/Buildings.js')
    exit()
if graph_rooms is None:
    print('Could not find assets_server/text/{0}_graph.txt'.format(building_shorthand))
    exit()

print('\nMissing from {0}_graph.txt:'.format(building_shorthand))
missing_rooms = building_rooms - graph_rooms
print_missing_rooms(missing_rooms)

print('\nMissing from Buildings.js:')
missing_rooms = graph_rooms - building_rooms
print_missing_rooms(missing_rooms)
print()
