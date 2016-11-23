import re
import sys
from bs4 import BeautifulSoup
from subprocess import run
from urllib.request import urlopen

# Configuration
verbose = False
output_files = []
errors = []

regex_departure_times = re.compile(r'<td class="xl66">([\d:]{5})</td>\s*<td class="xl66">([\d:]{5})</td>\s*</tr>')

# Check for system arguments
if '--verbose' in sys.argv or '-v' in sys.argv:
  verbose = True

# Prints a message if the verbose flag was provided
def print_verbose_message(*messages):
  if verbose:
    print(' SHUTTLE\t', ' '.join(messages))

shuttle_url = 'http://www.uottawa.ca/parking/shuttle-bus'

print_verbose_message('Opening url', shuttle_url)
url_response = urlopen(shuttle_url)
shuttle_html = url_response.read().decode('utf-8')

with open('temp_data/blah.txt', 'w', encoding='utf8') as outfile:
  outfile.write(shuttle_html)

with open('temp_data/blah2.txt', 'w', encoding='utf8') as outfile:
  outfile.write(shuttle_html)

run(['diff', '-u', 'temp_data/blah.txt', 'temp_data/blah2.txt'])
