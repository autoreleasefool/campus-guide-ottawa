import io
import requests
import sys
import zipfile

def updateData():
  print('Downloading data')
  zip_url = 'http://www.octranspo1.com/files/google_transit.zip'

  response = requests.get(zip_url)
  if response.status_code != 200:
    sys.exit(0)

  zipped_transit_data = zipfile.ZipFile(io.BytesIO(response.content))
  zipped_transit_data.extractall(path='temp_data/txt');

if '--update-info' in sys.argv or '-u' in sys.argv:
  updateData()

#
# Parsing
#