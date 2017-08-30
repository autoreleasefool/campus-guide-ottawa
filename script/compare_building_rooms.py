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
    with open(os.path.join('assets_app', 'js', 'Buildings.js')) as building_file:
        json_room_listing = set()
        line = building_file.readline()
        collect_rooms = False
        while line:
            name_pos = line.find(' name:')
            if name_pos > 0 and collect_rooms:
                room_name = line[name_pos + 8:line.find('\'', name_pos + 8)]
                json_room_listing.add('R{0}'.format(room_name))
            elif 'shorthand' in line:
                shorthand = line[line.find('shorthand') + 12:line.rfind('\'')]
                if shorthand == building_shorthand:
                    collect_rooms = True
                elif collect_rooms:
                    break
            line = building_file.readline()

    with open(os.path.join(
        'assets_server',
        'text',
        '{0}_graph.txt'.format(building_shorthand)
        )) as graph_file:
        graph_room_listing = set()
        line = graph_file.readline()
        while line:
            if re.match(r'^(R\d+)[|].*', line):
                graph_room_listing.add(line[:line.find('|')])
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
        print('\t{0}'.format(room_name[1:]))
        pass

building_rooms, graph_rooms = load_files()
if building_rooms is None:
    print('Could not find assets_app/js/Buildings.js')
    exit()
if graph_rooms is None:
    print('Could not find assets_server/text/{0}_graph.txt'.format(building_shorthand))
    exit()

print('Missing from {0}_graph.txt:'.format(building_shorthand))
missing_rooms = building_rooms - graph_rooms
print_missing_rooms(missing_rooms)

print('Missing from Buildings.js:')
missing_rooms = graph_rooms - building_rooms
print_missing_rooms(missing_rooms)
