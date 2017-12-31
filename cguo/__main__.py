"""Manage University of Ottawa Campus Guide app scripts."""


import argparse
import os
import sys
from .licenses.oss import get_oss_licenses
from .useful_links.verify import check_links


def get_asset_dir(component):
    """Get the asset directory path.

    :param component:
        either 'app' or 'server'
    :type component:
        `str`
    """
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        '..',
                        'assets_{}'.format(component))


def get_output_dir():
    """Get the output directory path."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        '..',
                        'output')


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
    os.makedirs(get_output_dir(), exist_ok=True)

    if parsed_args.compare:
        # TODO: setup compare_building_rooms script
        print('This script has not been merged.')
    elif parsed_args.courses:
        # TODO: setup campus_scraper script
        print('This script has not been merged.')
    elif parsed_args.licenses:
        get_oss_licenses(os.path.join(get_output_dir(), 'licenses.json'))
    elif parsed_args.links:
        check_links(os.path.join(get_asset_dir('server'), 'json', 'useful_links.json'))
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
