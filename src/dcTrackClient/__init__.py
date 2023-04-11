import requests


class Client:
    def __init__(self, baseUrl: str, username: str = '', password: str = '', apiToken: str = ''):
        """Provide either a username and password, or an API token to access the dcTrack database with Python."""
        self.__BASE_URL = baseUrl
        self.__USERNAME = username
        self.__PASSWORD = password
        self.__APITOKEN = apiToken

    def __request(self, method: str, endpoint: str, body: dict = None):
        if self.__USERNAME and self.__PASSWORD:
            return requests.request(method,  self.__BASE_URL + '/' + endpoint, json=body, auth=(self.__USERNAME, self.__PASSWORD)).json()
        elif self.__APITOKEN:
            return requests.request(method, self.__BASE_URL + '/' + endpoint, json=body, headers={'Authorization': 'Token ' + self.__APITOKEN}).json()
        else:
            raise Exception('Undefined username/password or token.')

    # Manage Items

    def createItem(self, data: dict, returnDetails: bool = True):
        """Create a new item."""
        return self.__request('POST', 'api/v2/dcimoperations/items?returnDetails=' + str(returnDetails).lower(), data)

    def modifyItem(self, id: int, data: dict, returnDetails: bool = True):
        """Update an existing item."""
        return self.__request('PUT', 'api/v2/dcimoperations/items/' + str(id) + '?returnDetails=' + str(returnDetails).lower(), data)

    def deleteItem(self, id: int):
        """Delete an item using the item ID."""
        return self.__request('DELETE', 'api/v2/dcimoperations/items/' + str(id))

    def getItem(self, id: int):
        """Get item details using the item ID."""
        return self.__request('GET', 'api/v2/dcimoperations/items/' + str(id))

    def quicksearch(self, data: dict, pageNumber: int, pageSize: int):
        """Search for items using criteria JSON object. Search criteria can be any of the fields applicable to items, including custom fields. Specify the fields to be included in the response. This API supports pagination."""
        return self.__request('POST', 'api/v2/quicksearch/items?pageNumber=' + str(pageNumber) + '&pageSize=' + str(pageSize), data)

    def getCabinetItems(self, cabId: int):
        """Returns a list of Items contained in a Cabinet using the ItemID of the Cabinet. The returned list includes all of the Cabinet's Items including Passive Items."""
        return self.__request('POST', 'api/v2/items/cabinetItems/' + str(cabId))

    def manageItemsBulk(self, cabId: int):
        """Retrieve a list of Items contained in a Cabinet including Passive Items."""
        return self.__request('POST', 'api/v2/items/cabinetItems/' + str(cabId))

    # Makes, Models, and Connectors

    def getAllMakes(self):
        """Retrieve a list of all Makes."""
        return self.__request('GET', '/api/v2/makes')

    def addMake(self, data: dict):
        """Add a new Make."""
        return self.__request('POST', '/api/v2/makes', data)

    def modifyMake(self, id: int, data: dict):
        """Modify a Make."""
        return self.__request('POST', '/api/v2/makes/' + str(id), data)

    def deleteMake(self, id: int):
        """Delete a Make."""
        return self.__request('POST', '/api/v2/makes/' + str(id))

    def getMakesByName(self, name: str, usingSpecialChars: bool = False):
        """Search for one or more makes using the make name. You also can search using special characters."""
        if usingSpecialChars:
            return self.__request('POST', '/api/v2/dcimoperations/search/list/makes', {'searchString', name})
        else:
            return self.__request('GET', '/api/v2/dcimoperations/search/makes/' + name)

    def getModel(self, id: int, usedCounts: bool = False):
        """Get Model fields for the specified Model ID."""
        return self.__request('GET', '/api/v2/models/' + str(id) + '?usedCounts=' + str(usedCounts).lower())

    def addModel(self, data: dict, returnDetails: bool = True, proceedOnWarning: bool = False):
        """Add a new Model."""
        return self.__request('POST', '/api/v2/models?returnDetails=' + str(returnDetails).lower() + '&proceedOnWarning=' + str(proceedOnWarning).lower(), data)

    def modifyModel(self, id: int, data: dict, returnDetails: bool = True, proceedOnWarning: bool = False):
        """Modify an existing Model."""
        return self.__request('PUT', '/api/v2/models/' + str(id) + '?returnDetails=' + str(returnDetails).lower() + '&proceedOnWarning=' + str(proceedOnWarning).lower(), data)

    def deleteModel(self, id: int):
        """Delete a Model using the Model ID."""
        return self.__request('DELETE', '/api/v2/models/' + str(id))

    def searchModels(self, data: dict, pageNumber: int, pageSize: int):
        """Search for models by user supplied search criteria."""
        return self.__request('POST', '/api/v2/quicksearch/models?pageNumber=' + str(pageNumber) + '&pageSize=' + str(pageSize), data)

    def getConnector(self, id: int, usedCount: bool = False):
        """Get a Connector record by ID."""
        return self.__request('GET', '/api/v2/settings/connectors/' + str(id) + '?usedCount=' + str(usedCount).lower())

    def addConnector(self, data: dict):
        """Add a new Connector."""
        return self.__request('POST', '/api/v2/settings/connectors', data)

    def updateConnector(self, id: int, data: dict):
        """Update an existing Connector."""
        return self.__request('PUT', '/api/v2/settings/connectors/' + str(id), data)

    def deleteConnector(self, ids: list[int]):
        """Delete one or more Connector records."""
        return self.__request('POST', '/api/v2/settings/connectors/delete', ids)

    def searchConnectors(self, data: dict, pageNumber: int, pageSize: int, usedCount: bool):
        """Retrieve a List of Connectors."""
        return self.__request('POST', '/api/v2/settings/connectors/quicksearch?pageNumber=' + str(pageNumber) + '&pageSize=' + str(pageSize) + '&usedCount=' + str(usedCount).lower(), data)
