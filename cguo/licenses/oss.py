"""Parse license files for Campus Guide application."""


import json
import os
import re
from collections import OrderedDict
import requests


def get_license_sources():
    """Filepath for open source license sources."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'json',
                        'sources.json')


def get_oss_licenses(output):
    """Get open source licenses and combine into single file.

    :param filename:
        location of the licensing source file.
    :type filename:
        `str`
    :param output:
        output location
    :type output:
        `str`
    """
    sources_json = None

    # Open the set of sources for modules
    with open(get_license_sources()) as sources:
        sources_json = json.loads(sources.read(), object_pairs_hook=OrderedDict)

    # If no sources were loaded, exit
    if sources_json is None:
        exit()

    # Final source to print
    licenses = []

    for source in sources_json:
        response = requests.get(sources_json[source])
        if response.status_code != 200:
            print('Request returned status code {}'.format(response.status_code))
            print('Could not retrieve license for source: {}'.format(source))
            exit()
        else:
            body = response.text
            body = re.sub(r'\r', '\n', body)
            body = re.sub(r'(?<!\n)\n(?!\n)', ' ', body)
            body = re.sub(r' {2,}', ' ', body)
            body = re.sub(r'(?<!\n)\n(?!\n)|\n{3,}', '', body)
            licenses.append({
                'key': source,
                'data': [{
                    'key': 0,
                    'text': body
                }]
            })
            print('Retrieved license for source {}'.format(source))

    licenses = sorted(licenses, key=lambda k: k['key'].lower())

    # os.makedirs('./output/', exist_ok=True)
    with open(output, 'w+', encoding='utf8') as outfile:
        json.dump(licenses, outfile, sort_keys=True, ensure_ascii=False)
