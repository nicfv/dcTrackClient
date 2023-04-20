# dcTrackClient ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/nicfv/dcTrackClient/python-publish.yml?label=publish&logo=pypi) ![PyPI](https://img.shields.io/pypi/v/dcTrackClient) ![PyPI - Downloads](https://img.shields.io/pypi/dm/dcTrackClient)

Sunbird [dcTrack](https://www.sunbirddcim.com/) API client in Python

## Initialize a connection to the dcTrack API

Import the class:

```py
from dcTrackClient import Client
```

Authenticate using a base URL (the same URL to access the GUI) and a username and password:

```py
api = Client('https://dctrack.example.com/', username='user', password='pass')
```

Authenticate using a base URL and an API token:

```py
api = Client('https://dctrack.example.com/', apiToken='asdf')
```

## Usage Example

### Create an item:

- This example shows the minimum attributes required to create an item
- See [the official documentation](#official-dctrack-documentation) for a comprehensive list of attributes
- This function returns the JSON object for the newly created item
- If it fails, the function will return a JSON object containing the error message

```py
api.createItem({'cmbLocation': 'SAMPLE LOCATION', 'tiName': 'NEW-ITEM', 'cmbMake': 'Generic', 'cmbModel': 'Generic^Rackable^01'})
```

### Retrieve item details:

```py
item = api.getItem(1234)
```

Returns:

```json
{
    "item": {
        ... // item attributes in here
    }
}
```

### Modify an existing item:

```py
api.modifyItem(1234, {'tiSerialNumber': 'SN-12345', 'tiAssetTag': 'DEV-12345'})
```

### Delete an existing item:

```py
api.deleteItem(1234)
```

## Official DcTrack Documentation

Visit this link for the official documentation on request bodies and attrribute names.

https://www.sunbirddcim.com/help/dcTrack/v900/API/en/Default.htm
