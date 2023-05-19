**WARNING: this project is still under development and may not be stable!**

# dcTrackClient [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/nicfv/dcTrackClient/publish.yml?logo=github)](https://github.com/nicfv/dcTrackClient) [![PyPI](https://img.shields.io/pypi/v/dcTrackClient)](https://pypi.org/project/dcTrackClient/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/dcTrackClient?logo=pypi)](https://pypi.org/project/dcTrackClient/) [![npm](https://img.shields.io/npm/v/dctrackclient)](https://www.npmjs.com/package/dctrackclient) [![npm](https://img.shields.io/npm/dt/dctrackclient?logo=npm)](https://www.npmjs.com/package/dctrackclient)
Sunbird [dcTrack](https://www.sunbirddcim.com/) API clients in Python and JavaScript

## Installation
> dcTrackClient can be installed from the package manager of your choice.

### Python
```shell
pip install dcTrackClient==%VERSION%
```

### JavaScript
```shell
npm i dctrackclient@%VERSION%
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
import { Client } from 'dctrackclient';
// Using a username and password // 
const api = new Client('https://dctrack.example.com/', { username: 'user', password: 'pass' });
// Using an API token //
const api = new Client('https://dctrack.example.com/', { apiToken: 'token' });
```

# Usage Example
This section demonstrates item manipulation with the API client.

## Create an item
> This example shows the minimum attributes required to create an item using the [`createItem`](#createitemreturndetails-payload) function. View the comprehensive list of item attributes in the [official documentation](https://www.sunbirddcim.com/help/dcTrack/v900/API/en/Default.htm#APIGuide/REST_API_JSON_Objects_for_Managed_Items.htm). Make sure to capture the return value of this function to see the created item details, such as the unique numeric item ID, or to determine if an error occurred while creating an item.

### Python
```py
response = api.createItem(True/False, {
    'cmbLocation': 'item location',
    'tiName': 'item name',
    'cmbMake': 'item make',
    'cmbModel': 'item model'
})
print(response)
```

### JavaScript
Notice the `await` keyword before the function call. This is because the JavaScript library is asynchronous and returns a `Promise` to the return value. All the API calls in this library require that keyword.
```js
let response = await api.createItem(true/false, {
    'cmbLocation': 'item location',
    'tiName': 'item name',
    'cmbMake': 'item make',
    'cmbModel': 'item model'
});
console.log(response);
```

### On Success
This function returns the JSON object for the newly created item. This is an example response if `returnDetails` was set to false.
```json
{ "item": { "id": 1234, "tiName": "item name" } }
```

### On Failure
This function returns a JSON object containing the error message.

## Retrieve item details
> This example shows the usage of the [`getItem`](#getitemid) function.

### Python
```py
response = api.getItem(1234)
```

### JavaScript
```js
let response = await api.getItem(1234);
```

### Returns
```json
{
    "item": {
        "cmbLocation": "item location",
        "tiName": "item name",
        ...
    }
}
```

## Modify an existing item
> This example shows the usage of the [`updateItem`](#updateitemid-returndetails-payload) function. Any number of attributes can be included in the payload to be modified.

### Python
```py
response = api.updateItem(1234, False, {'tiSerialNumber': 12345})
```

### JavaScript
```js
let response = await api.updateItem(1234, false, { 'tiSerialNumber': 12345 });
```

## Search for an item
> This example demonstrates usage of the [`searchItems`](#searchitemspagenumber-pagesize-payload) function. Follow [this guide](https://www.sunbirddcim.com/help/dcTrack/v900/API/en/Default.htm#APIGuide/v2_Advanced_Search_API.htm) for details on creating the request payload.

### Python
```py
response = api.searchItems(0, 0, {
    'columns': [
        {'name': 'tiName', 'filter': {'eq': 'item name'}}
    ],
    'selectedColumns': [
        {'name': 'id'},
        {'name': 'tiName'},
    ]
})
```

### JavaScript
```js
let response = await api.searchItems(0, 0, {
    'columns': [
        { 'name': 'tiName', 'filter': { 'eq': 'item name' } }
    ],
    'selectedColumns': [
        { 'name': 'id' },
        { 'name': 'tiName' },
    ]
});
```

### Returns
```json
{
    "selectedColumns": [],
    "totalRows": 1,
    "pageNumber": 0,
    "pageSize": 0,
    "searchResults": {
        "items": [
            {"id": "1234", "tiName": "item name"}
        ]
    }
}
```

## Delete an item
> This example demonstrates usage of the [`deleteItem`](#deleteitemid) function.

### Python
```py
api.deleteItem(1234)
```

### JavaScript
```js
await api.deleteItem(1234);
```

### Returns
```json
{ "itemId": 1234 }
```

# Official DcTrack Documentation

Visit this link for the official documentation on request bodies and attrribute names.

https://www.sunbirddcim.com/help/dcTrack/v900/API/en/Default.htm

# Package Documentation

The section below shows all the functions contained within this client along with basic usage.
