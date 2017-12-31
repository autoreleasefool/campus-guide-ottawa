"""
Push or pull assets to or from working directories for the application
and backend of the Campus Guide app.
"""


import argparse
import logging
import os
import re
import shutil
import sys
from ..util.path import get_asset_dir


LOGGER = logging.getLogger()
LOGGER.addHandler(logging.StreamHandler(sys.stdout))


def is_ignored(filename, ignores):
    """
    Checks if the filename matches any of the ignored keywords

    :param filename:
        The filename to check
    :type filename:
        `str`
    :param ignores:
        List of regex paths to ignore. Can be none
    :type ignores:
        `list` of `str` or None
    :rtype:
        `bool`
    """
    return ignores and len([x for x in ignores if re.search(x, filename)]) > 0


def push_assets(source, dest, ignores, depth=0):
    """
    Recursively copy assets from the source directory to the destination.

    :param source:
        Source directory to copy from
    :type source:
        `str`
    :param dest:
        Destination directory to copy to
    :type dest:
        `str`
    :param ignores:
        List of regex paths to ignore. Can be none
    :type ignores:
        `list` of `str` or None
    :param depth:
        Recursion depth
    :type depth:
        `int`
    """
    indent = ' ' * depth
    directories = []

    if dest.startswith('./assets_server/') or dest.startswith('./assets_app/'):
        LOGGER.debug('%s Removing destination if exists', indent)
        if os.path.exists(dest):
            shutil.rmtree(dest)

    LOGGER.debug('%s Creating destination directory', indent)
    if not os.path.exists(dest):
        os.makedirs(dest)

    LOGGER.debug('%s Pushing assets from `%s` to `%s`', indent, source, dest)
    for file in os.listdir(source):
        if file.startswith('.'):
            continue

        source_path = os.path.join(source, file)
        dest_path = os.path.join(dest, file)

        if is_ignored(source_path, ignores):
            continue

        if os.path.isfile(source_path):
            LOGGER.debug('%s  Copying file `%s` to `%s`', indent, source_path, dest_path)
            # Copy files to the destination directory
            shutil.copy(source_path, dest_path)
        else:
            directories.append(file)

    for directory in directories:
        source_path = os.path.join(source, directory)
        dest_path = os.path.join(dest, directory)

        # Recursively push assets in directories
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
        push_assets(source_path, dest_path, ignores, depth + 1)


def update_assets(args, app_dir, server_dir):
    """Update assets."""
    if args is None:
        args = []

    default_ignores = ['__schemas__', '__tests__']

    arg_parser = argparse.ArgumentParser(description='Update app and server assets.')
    arg_parser.add_argument('--pull-server',
                            action='store_true',
                            help='pull the assets from campus-guide-backend to this repository')
    arg_parser.add_argument('--push-server',
                            action='store_true',
                            help='push the assets from this repository to campus-guide-backend')
    arg_parser.add_argument('--pull-app',
                            action='store_true',
                            help='pull the assets from campus-guide to this repository')
    arg_parser.add_argument('--push-app',
                            action='store_true',
                            help='push the assets from this repository to campus-guide')
    arg_parser.add_argument('--app',
                            default=app_dir,
                            help='Set the location for `campus-guide`')
    arg_parser.add_argument('--server',
                            default=server_dir,
                            help='Set the location for `campus-guide-server`.')
    arg_parser.add_argument('--ignore',
                            nargs='*',
                            help='Ignore a pattern and do not push/pull assets matching it',
                            default=default_ignores)
    arg_parser.add_argument('-v', '--verbose',
                            action='store_true',
                            help='provide in depth logs as the tool executes')
    parsed_args = arg_parser.parse_args(args)

    LOGGER.setLevel(logging.DEBUG if parsed_args.verbose else logging.INFO)

    # Exit if directory args are not valid
    if not os.path.isdir(parsed_args.app):
        LOGGER.info('`%s` is not a directory. Exiting.')
        sys.exit(1)
    elif not os.path.isdir(parsed_args.server):
        LOGGER.info('`%s` is not a directory. Exiting.')
        sys.exit(1)

    dest_app_dir = os.path.join(parsed_args.app, 'assets')
    dest_server_dir = os.path.join(parsed_args.server, 'assets')
    source_app_dir = get_asset_dir('app')
    source_server_dir = get_asset_dir('server')

    if parsed_args.push_server and not parsed_args.pull_server:
        if not os.path.exists(dest_server_dir):
            os.makedirs(dest_server_dir)
        LOGGER.info('Pushing server assets to `%s`', dest_server_dir)
        push_assets(source_server_dir, dest_server_dir, parsed_args.ignore)
    elif parsed_args.pull_server and not parsed_args.push_server:
        LOGGER.info('Pulling server assets from `%s`', dest_server_dir)
        push_assets(dest_server_dir, source_server_dir, parsed_args.ignore)
    elif parsed_args.pull_server and parsed_args.push_server:
        LOGGER.info('Cannot push and pull server assets simultaneously. Skipping.')

    if parsed_args.push_app and not parsed_args.pull_app:
        if not os.path.exists(dest_app_dir):
            os.makedirs(dest_app_dir)
        LOGGER.info('Pushing app assets to `%s`', dest_app_dir)
        push_assets(source_app_dir, dest_app_dir, parsed_args.ignore)
    elif parsed_args.pull_app and not parsed_args.push_app:
        LOGGER.info('Pulling app assets from `%s`', dest_app_dir)
        push_assets(dest_app_dir, source_app_dir, parsed_args.ignore)
    elif parsed_args.pull_app and parsed_args.push_app:
        LOGGER.info('Cannot push and pull app assets simultaneously. Skipping.')
