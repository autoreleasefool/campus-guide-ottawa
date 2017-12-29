import re
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Configuration
verbose = False
output_files = []
errors = []

regex_time = re.compile(r'([0-1][0-9]|2[0-3]|[0-9]):([0-5][0-9])')

# Check for system arguments
if '--verbose' in sys.argv or '-v' in sys.argv:
  verbose = True

# Prints a message if the verbose flag was provided
def print_verbose_message(*messages):
  if verbose:
    print(' SHUTTLE\t', ' '.join(messages))

def normalize_time(time):
  return time if time[2] == ':' else '0' + time

schedules = []
shuttle_url_en = 'http://www.uottawa.ca/parking/shuttle-bus'
shuttle_url_fr = 'https://www.uottawa.ca/stationnement/navette'

def sanitize(input):
  return input.replace(u'\xa0', u' ').replace(u'\n', u' ').replace(u'\t', u' ')

# English shuttle information

print_verbose_message('Opening url', shuttle_url_en)
url_response = urlopen(shuttle_url_en)
shuttle_html = url_response.read().decode('utf-8')
shuttle_soup = BeautifulSoup(shuttle_html, 'html.parser')

schedule_index = 0
for table in shuttle_soup.find_all('table'):
  if table.thead:
    titleContainer = table.parent.parent.parent.parent
    title = titleContainer.h2 if titleContainer.h2 else titleContainer.summary
    schedules.append({
      'name_en': sanitize(title.text),
      'departures': []
    })
    for header in table.thead.tr.find_all('th'):
      schedules[schedule_index]['departures'].append({
        'name_en': sanitize(header.text),
        'times': []
      })
    for row in table.tbody.find_all('tr'):
      for index, value in enumerate(row.find_all('td')):
        if regex_time.search(value.text):
          schedules[schedule_index]['departures'][index]['times'].append(normalize_time(sanitize(value.text)))

    schedule_index += 1

# French shuttle information

print_verbose_message('Opening url', shuttle_url_fr)
url_response = urlopen(shuttle_url_fr)
shuttle_html = url_response.read().decode('utf-8')
shuttle_soup = BeautifulSoup(shuttle_html, 'html.parser')

schedule_index = 0
for table in shuttle_soup.find_all('table'):
  if table.thead:
    titleContainer = table.parent.parent.parent.parent
    title = titleContainer.h2 if titleContainer.h2 else titleContainer.summary
    schedules[schedule_index]['name_fr'] = sanitize(title.text)
    for index, header in enumerate(table.thead.tr.find_all('th')):
      schedules[schedule_index]['departures'][index]['name_fr'] = sanitize(header.text)

    schedule_index += 1

import json
print(json.dumps(schedules, sort_keys=True, indent=2))

