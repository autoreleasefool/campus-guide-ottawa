"""Manage University of Ottawa Campus Guide app scripts."""


import argparse
import sys


def main(args=None):
    """Main method."""
    if args is None:
        args = sys.argv[1:]

    base_args = args[0:1]
    script_args = args[1:] if len(args) > 2 else None

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

    if parsed_args.compare:
        # TODO: setup compare_building_rooms script
        print('This script has not been merged.')
    elif parsed_args.courses:
        # TODO: setup campus_scraper script
        print('This script has not been merged.')
    elif parsed_args.licenses:
        # TODO: setup licenses.py script
        print('This script has not been merged.')
    elif parsed_args.links:
        # TODO: setup dead link checker
        print('This script has not been merged.')
    elif parsed_args.shuttle:
        # TODO: setup shuttle script
        print('This script has not been merged.')
    elif parsed_args.transit:
        # TODO: setup transit script
        print('This script has not been merged.')
    elif parsed_args.update_assets:
        # TODO: setup update_assets script
        print('This script has not been merged.')
    else:
        print('No script provided. Use -h for help.')
        sys.exit(0)


if __name__ == '__main__':
    main()
