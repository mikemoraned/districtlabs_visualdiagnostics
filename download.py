import os
import zipfile
import requests

OCCUPANCY = ('http://bit.ly/ddl-occupancy-dataset', 'occupancy.zip')
CREDIT    = ('http://bit.ly/ddl-credit-dataset', 'credit.xls')
CONCRETE  = ('http://bit.ly/ddl-concrete-data', 'concrete.xls')

def download_data(url, name, path='data'):
    if not os.path.exists(path):
        os.mkdir(path)

    response = requests.get(url)
    with open(os.path.join(path, name), 'wb') as f:
        f.write(response.content)


def download_all(path='data'):
    for href, name in (OCCUPANCY, CREDIT, CONCRETE):
        download_data(href, name, path)

    # Extract the occupancy zip data
    z = zipfile.ZipFile(os.path.join(path, 'occupancy.zip'))
    z.extractall(os.path.join(path, 'occupancy'))

path='data'
download_all(path)
