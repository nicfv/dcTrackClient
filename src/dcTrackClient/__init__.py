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
            return requests.request(method,  self.__BASE_URL + endpoint, json=body, auth=(self.__USERNAME, self.__PASSWORD)).json()
        elif self.__APITOKEN:
            return requests.request(method, self.__BASE_URL + endpoint, json=body, headers={'Authorization': 'Token ' + self.__APITOKEN}).json()
        else:
            raise Exception('Undefined username/password or token.')

    def createItem(self, data: dict):
        """Create an item"""
        return self.__request('POST', 'api/v2/dcimoperations/items?returnDetails=true', data)

    def modifyItem(self, id: int, data: dict):
        """Modify an item"""
        return self.__request('PUT', 'api/v2/dcimoperations/items/' + str(id) + '?returnDetails=true', data)

    def deleteItem(self, id: int):
        """Delete an item"""
        return self.__request('DELETE', 'api/v2/dcimoperations/items/' + str(id))

    def getItem(self, id: int):
        """Get item details by ID"""
        return self.__request('GET', 'api/v2/dcimoperations/items/' + str(id))

    def quicksearch(self, page: int, data: dict):
        """Search for items by specifying search criteria on available item attributes, including a multi-field search."""
        return self.__request('POST', 'api/v2/quicksearch/items?pageSize=0&pageNumber=' + str(page), data)

    def getCabinetItems(self, cabId: int):
        """Retrieve a list of Items contained in a Cabinet including Passive Items."""
        return self.__request('POST', 'api/v2/items/cabinetItems/' + str(cabId))
