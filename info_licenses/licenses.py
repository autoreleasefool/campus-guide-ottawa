import json
import os
import requests
from collections import OrderedDict

sources_json = None

# Open the set of sources for modules
with open('./json/sources.json') as sources:
  sources_json = json.loads(sources.read(), object_pairs_hook=OrderedDict)

# If no sources were loaded, exit
if sources_json is None:
  exit()

# Final source to print
licenses = ''

for source in sources_json:
  response = requests.get(sources_json[source])
  if response.status_code != 200:
    print('Request returned status code {0}'.format(response.status_code))
    print('Could not retrieve license for source: {0}'.format(source))
    exit()
  else:
    licenses += '<b>{0}</b><br />'.format(source)
    body = response.text.replace('"', '\\"')
    body = body.replace('\n', '<br />')
    licenses += body

os.makedirs('./output/', exist_ok=True)
with open('./output/licenses.txt', 'w+', encoding='utf8') as outfile:
  outfile.write(licenses)
