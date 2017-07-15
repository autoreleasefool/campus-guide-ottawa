#!/usr/bin/env python3

"""
Push or pull assets to or from working directories for the application
and backend of the Campus Guide app.
"""

import os
import re
import shutil
import sys

# Output instructions to use the scraper, then exit
if len(sys.argv) == 1:
    print('\nUse this tool to update your campus-guide and campus-guide-server assets.')
    print('\t--pull-server\t\tPull the assets from campus-guide-server to this repository')
    print('\t--pull-app\t\tPull the assets from campus-guide to this repository')
    print('\t--push-server\t\tPush the assets from this repository to campus-guide-server')
    print('\t--push-app\t\tPush the assets from this repository to campus-guide')
    print('\t--app <directory>\tSet the location for `campus-guide`. Default is `../campus-guide`')
    print('\t--server <directory>\tSet the location for `campus-guide-server`.' +
          'Default is `../campus-guide-server`')
    print('\t--ignore <pattern>\tIgnore a pattern and do not push/pull assets matching it')
    print('\t--verbose, -v\t\tProvide in depth logs as the tool executes')
    print()
    exit()

if os.getcwd().split(os.sep)[-1] != 'campus-guide-ottawa':
    print('\nYou must use this script from the `campus-guide-ottawa` directory.\n')
    exit()

# Set default arguments
VERBOSE = False
IGNORES = ['__schemas__', '__tests__']


def print_verbose_message(message):
    """
    Prints a message only if verbose mode is enabled.

    :param message:
        The message to print
    :type message:
        `str`
    """
    if VERBOSE:
        print(message)

APP_DIRECTORY = '../campus-guide'
PULL_APP = False
PUSH_APP = False

SERVER_DIRECTORY = '../campus-guide-backend'
PULL_SERVER = False
PUSH_SERVER = False


def is_ignored(filename):
    """
    Checks if the filename matches any of the ignored keywords

    :param filename:
        The filename to check
    :type filename:
        `str`
    :rtype:
        `bool`
    """
    return len([x for x in IGNORES if re.search(x, filename)]) > 0


def push_assets(source, dest, depth=0):
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
    :param depth:
        Recursion depth
    :type depth:
        `int`
    """
    indent = ' ' * depth
    directories = []

    if dest.startswith('./assets_server/') or dest.startswith('./assets_app/'):
        print_verbose_message(indent + ' Removing destination if exists')
        if os.path.exists(dest):
            shutil.rmtree(dest)

    print_verbose_message(indent + ' Creating destination directory')
    if not os.path.exists(dest):
        os.makedirs(dest)

    print_verbose_message(indent + ' Pushing assets from `' + source + '` to `' + dest + '`')
    for file in os.listdir(source):
        if file.startswith('.'):
            continue

        source_path = os.path.join(source, file)
        dest_path = os.path.join(dest, file)

        if is_ignored(source_path):
            continue

        if os.path.isfile(source_path):
            print_verbose_message('{0}  Copying file `{1}` to `{2}`'.format(
                indent,
                source_path,
                dest_path,
            ))
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
        push_assets(source_path, dest_path, depth + 1)

for i, arg in enumerate(sys.argv):
    if not arg.startswith('-'):
        continue

    # General argument parsing
    if not VERBOSE and arg == '-v' or arg == '--verbose':
        VERBOSE = True
    elif arg == '--ignore' and i < len(sys.argv) - 1:
        IGNORES.append(sys.argv[i + 1])

    # App argument parsing
    elif arg == '--app' and i < len(sys.argv) - 1:
        if os.path.isdir(sys.argv[i + 1]):
            APP_DIRECTORY = sys.argv[i + 1]
        else:
            print('`' + sys.argv[i + 1] + '` is not a directory. Exiting.')
            exit()
    elif not PULL_APP and arg == '--pull-app':
        PULL_APP = True
    elif not PUSH_APP and arg == '--push-app':
        PUSH_APP = True

    # Server argument parsing
    elif arg == '--server' and i < len(sys.argv) - 1:
        if os.path.isdir(sys.argv[i + 1]):
            SERVER_DIRECTORY = sys.argv[i + 1]
        else:
            print('`' + sys.argv[i + 1] + '` is not a directory. Exiting.')
            exit()
    elif not PULL_SERVER and arg == '--pull-server':
        PULL_SERVER = True
    elif not PUSH_SERVER and arg == '--push-server':
        PUSH_SERVER = True

# Add path to assets
APP_DIRECTORY = os.path.join(APP_DIRECTORY, 'assets')
SERVER_DIRECTORY = os.path.join(SERVER_DIRECTORY, 'assets')

if PUSH_SERVER and not PULL_SERVER:
    if not os.path.exists(SERVER_DIRECTORY):
        os.makedirs(SERVER_DIRECTORY)
    print('Pushing server assets to `' + SERVER_DIRECTORY + '`')
    push_assets('./assets_server/', SERVER_DIRECTORY)
elif PULL_SERVER and not PUSH_SERVER:
    print('Pulling server assets from `' + SERVER_DIRECTORY + '`')
    push_assets(SERVER_DIRECTORY, './assets_server/')
elif PUSH_SERVER and PULL_SERVER:
    print('Cannot push and pull server assets simultaneously. Skipping.')

if PUSH_APP and not PULL_APP:
    if not os.path.exists(APP_DIRECTORY):
        os.makedirs(APP_DIRECTORY)
    print('Pushing app assets to `' + APP_DIRECTORY + '`')
    push_assets('./assets_app/', APP_DIRECTORY)
elif PULL_APP and not PUSH_APP:
    print('Pulling app assets from `' + APP_DIRECTORY + '`')
    push_assets(APP_DIRECTORY, './assets_app/')
elif PUSH_APP and PULL_APP:
    print('Cannot push and pull app assets simultaneously. Skipping.')
