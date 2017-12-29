"""Verify useful links are still valid."""

import json
import requests


def add_link(link, valid, invalid):
    """Add a link to either the valid or invalid list."""
    list_to_add_to = valid

    # Skip the link if it's invalid
    if 'invalid' in link and link['invalid']:
        list_to_add_to = invalid

    if 'link' in link and not link['link'].startswith('tel:'):
        list_to_add_to.append(link['link'])
    if 'link_en' in link and not link['link_en'].startswith('tel:'):
        list_to_add_to.append(link['link_en'])
    if 'link_fr' in link and not link['link_fr'].startswith('tel:'):
        list_to_add_to.append(link['link_fr'])


def retrieve_links(categories, valid, invalid):
    """Iterate over all the links in a list of categories."""
    # Iterate over each category
    for category in categories:

        # Iterate over the default links in the category
        if 'links' in category:
            for link in category['links']:
                add_link(link, valid, invalid)

        # Iterate over the social media links
        if 'social' in category:
            for link in category['social']:
                add_link(link, valid, invalid)

        # Iterate over any subcategories
        if 'categories' in category:
            retrieve_links(category['categories'], valid, invalid)


def main():
    """Main."""
    # pylint:disable=W0703

    # List of links to check
    links = []
    # Number of links checked so far
    links_checked = 0
    # List of links which failed to resolve
    failed_links = []
    # List of links which threw errors
    error_links = []
    # List of links which are invalid
    invalid_links = []

    # Open the set of links
    with open('./assets_server/json/useful_links.json') as useful_links:
        links_json = json.loads(useful_links.read())
        retrieve_links(links_json, links, invalid_links)

    # Iterate over each link and print the result of requesting it
    print('Total links to check:', len(links))
    for link in links:
        links_checked += 1
        print('(', links_checked, '/', len(links), ') ', sep='', end='')
        try:
            response = requests.get(link, verify=False, timeout=10)
            if response.status_code != 200:
                failed_links.append(link)
                print('Link failed: (', response.status_code, ') ', link, sep='')
            else:
                print('Link passed:', link)
        except (KeyboardInterrupt, SystemExit):
            raise
        except requests.exceptions.Timeout:
            error_links.append(link)
            print('Error, timed out:', link)
        except Exception:
            error_links.append(link)
            print('Error validating link:', link)

    # At the end, print links that failed
    print('------------------------------')
    print('Total failed links:', len(failed_links))
    for failed in failed_links:
        print('Failed:', failed)

    # At the end, prints links that threw an error
    print('------------------------------')
    print('Total error links:', len(error_links))
    for error in error_links:
        print('Error:', error)

    # At the end, prints links that were marked invalid
    print('------------------------------')
    print('Total invalid links:', len(invalid_links))
    for invalid in invalid_links:
        print('Invalid:', invalid)


if __name__ == '__main__':
    main()
