#!/usr/bin/env python3

import os
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
  print('\t--server <directory>\tSet the location for `campus-guide-server`. Default is `../campus-guide-server`')
  print('\t--verbose, -v\t\tProvide in depth logs as the tool executes')
  print()
  exit()

if os.getcwd().split(os.sep)[-1] != 'campus-guide-ottawa':
  print('\nYou must use this script from the `campus-guide-ottawa` directory.\n')
  exit()

# Prints a message if the verbose flag was provided
def print_verbose_message(message):
  if verbose:
    print(message)

# Set default arguments
verbose = False

app_directory = '../campus-guide'
pull_app = False
push_app = False

server_directory = '../campus-guide-server'
pull_server = False
push_server = False

def push_assets(source, dest, depth = 0):
  indent = ' ' * depth
  directories = []

  print_verbose_message(indent + ' Pushing assets from `' + source + '` to `' + dest + '`')
  for f in os.listdir(source):
    if (f.startswith('.')): continue

    source_path = os.path.join(source, f)
    dest_path = os.path.join(dest, f)

    if os.path.isfile(source_path):
      print_verbose_message(indent + '  Copying file `' + source_path + '` to `' + dest_path + '`')
      # Copy files to the destination directory
      shutil.copy(source_path, dest_path)
    else:
      directories.append(f)

  for d in directories:
    source_path = os.path.join(source, d)
    dest_path = os.path.join(dest, d)

    # Recursively push assets in directories
    if not os.path.exists(dest_path):
      os.mkdir(dest_path)
    push_assets(source_path, dest_path, depth + 1)

for i, arg in enumerate(sys.argv):
  if not arg.startswith('-'): continue

  # General argument parsing
  if not verbose and arg == '-v' or arg == '--verbose':
    verbose = True

  # App argument parsing
  elif arg == '--app':
    if os.path.isdir(sys.argv[i + 1]):
      app_directory = sys.argv[i + 1]
    else:
      print('`' + sys.argv[i + 1] + '` is not a directory. Exiting.')
      exit()
  elif not pull_app and arg == '--pull-app':
    pull_app = True
  elif not push_app and arg == '--push-app':
    push_app = True

  # Server argument parsing
  elif arg == '--server':
    if os.path.isdir(sys.argv[i + 1]):
      server_directory = sys.argv[i + 1]
    else:
      print('`' + sys.argv[i + 1] + '` is not a directory. Exiting.')
      exit()
  elif not pull_server and arg == '--pull-server':
    pull_server = True
  elif not push_server and arg == '--push-server':
    push_server = True

# Add path to assets
app_directory = os.path.join(app_directory, 'assets')
server_directory = os.path.join(server_directory, 'src', 'assets') 

if push_server and not pull_server:
  if not os.path.exists(server_directory):
    os.makedirs(server_directory)
  print('Pushing server assets to `' + server_directory + '`')
  push_assets('./assets_server/', server_directory)
elif pull_server and not push_server:
  print('Pulling server assets from `' + server_directory + '`')
  push_assets(server_directory, './assets_server/')
elif push_server and pull_server:
  print('Cannot push and pull server assets simultaneously. Skipping.')

if push_app and not pull_app:
  if not os.path.exists(app_directory):
    os.makedirs(app_directory)
  print('Pushing app assets to `' + app_directory + '`')
  push_assets('./assets_app/', app_directory)
elif pull_app and not push_app:
  print('Pulling app assets from `' + app_directory + '`')
  push_assets(app_directory, './assets_app/')
elif push_app and pull_app:
  print('Cannot push and pull app assets simultaneously. Skipping.')