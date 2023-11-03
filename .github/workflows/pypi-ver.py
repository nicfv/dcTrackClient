import requests
import sys

print(requests.get('https://pypi.org/pypi/' + sys.argv[1] + '/json').json()['info']['version'])
