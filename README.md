**WARNING: this project is still under development and may not be stable!**

# dcTrackClient [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/nicfv/dcTrackClient/publish.yml?logo=github)](https://github.com/nicfv/dcTrackClient) [![PyPI](https://img.shields.io/pypi/v/dcTrackClient)](https://pypi.org/project/dcTrackClient/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/dcTrackClient?logo=pypi)](https://pypi.org/project/dcTrackClient/) [![npm](https://img.shields.io/npm/v/dctrackclient)](https://www.npmjs.com/package/dctrackclient) [![npm](https://img.shields.io/npm/dt/dctrackclient?logo=npm)](https://www.npmjs.com/package/dctrackclient)

Sunbird [dcTrack](https://www.sunbirddcim.com/) API clients in Python and JavaScript

## Installation

> dcTrackClient can be installed from the package manager of your choice.

### Python

```
pip install dcTrackClient
```

### JavaScript

```
npm i dctrackclient
```

## Initialize a connection to the dcTrack API

> Authentication is by using a base URL (the same URL to access the GUI) and a username and password, or a base URL and an API token.

### Python

```py
from dcTrackClient import Client
## Using a username and password ##
api = Client('https://dctrack.example.com/', username='user', password='pass')
## Using an API token ##
api = Client('https://dctrack.example.com/', apiToken='token')
```

### JavaScript

```js
import * as api from 'dctrackclient';
// Using a username and password // 
api.Client.authenticate('https://dctrack.example.com/', { username: 'user', password: 'pass' });
// Using an API token //
api.Client.authenticate('https://dctrack.example.com/', { apiToken: 'token' });
```

## Usage Example

> This section is currently under construction.

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
