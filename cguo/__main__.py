"""Manage University of Ottawa Campus Guide app scripts."""


import argparse
import os
import sys
from .assets.compare_building_rooms import compare_rooms
from .assets.update_assets import update_assets
from .licenses.oss import get_oss_licenses
from .transit_times.transit_times import parse_transit_times
from .useful_links.verify import check_links
from .util.path import get_asset_dir, get_output_dir, get_root_dir


def main(args=None):
    """Main method."""
    if args is None:
        args = sys.argv[1:]

    base_args = args[0:1]
    script_args = args[1:] if len(args) > 1 else None

    arg_parser = argparse.ArgumentParser(description='Campus Guide Scripts (University of Ottawa)')
    arg_parser.add_argument('--compare',
                            action='store_true',
                            help='Compare rooms in Buildings.json and graph')
    arg_parser.add_argument('--courses',
                            action='store_true',
                            help='Course/exam/discipline scraping')
    arg_parser.add_argument('--licenses',
                            action='store_true',
                            help='Open source license attributions')
    arg_parser.add_argument('--links',
                            action='store_true',
                            help='Dead link checker')
    arg_parser.add_argument('--shuttle',
                            action='store_true',
                            help='Shuttle bus schedule scraper')
    arg_parser.add_argument('--transit',
                            action='store_true',
                            help='Transit time scraper')
    arg_parser.add_argument('--update-assets',
                            action='store_true',
                            help='Push or pull assets from the respective repository')

    parsed_args = arg_parser.parse_args(base_args)
    os.makedirs(get_output_dir(), exist_ok=True)

    if parsed_args.compare:
        compare_rooms(script_args)
    elif parsed_args.licenses:
        get_oss_licenses(os.path.join(get_output_dir(), 'licenses.json'))
    elif parsed_args.links:
        check_links(os.path.join(get_asset_dir('server'), 'json', 'useful_links.json'))
    elif parsed_args.update_assets:
        update_assets(script_args,
                      os.path.join(get_root_dir(), '..', 'campus-guide'),
                      os.path.join(get_root_dir(), '..', 'campus-guide-backend'))
    elif parsed_args.courses:
        # TODO: setup campus_scraper script
        print('This script has not been merged.')
    elif parsed_args.shuttle:
        # TODO: setup shuttle script
        print('This script has not been merged.')
    elif parsed_args.transit:
        parse_transit_times(script_args, os.path.join(get_output_dir(), 'transit.json'))
    else:
        print('No script provided. Use -h for help.')
        sys.exit(0)


if __name__ == '__main__':
    main()
