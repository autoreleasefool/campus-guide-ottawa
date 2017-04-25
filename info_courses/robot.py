from urllib.request import urlopen

# Configuration
verbose = False

# Update the level of verbosity to use (either True or False)
def set_verbosity(verbosity):
  global verbose
  verbose = verbosity

# Prints a message if the verbose flag was provided
def print_verbose_message(*messages):
  if verbose:
    print(' ROBO\t', ' '.join(messages))

# Iterate over lines in a robots.txt file and save them to a map
def parse_robot_txt(txt):
  params = {}
  for line in txt.split('\n'):
    if len(line) == 0: continue
    if line[0] == '#': continue

    key = line[0:line.index(':')]
    value = line[line.index(':') + 1:].strip()

    if key not in params:
      params[key] = [value]
    else:
      params[key].append(value)

  return params

# Retrieves robots.txt from the university and returns a parsing of it
def get():
  print_verbose_message('Retrieving robots.txt')
  url = 'http://www.uottawa.ca/robots.txt'

  print_verbose_message('Opening url:', url)
  robot_txt = urlopen(url).read().decode('utf-8')

  return parse_robot_txt(robot_txt)