import requests, sys

print(requests.get('https://pypi.org/pypi/' + sys.argv[1] + '/json').json()['info']['version'])
