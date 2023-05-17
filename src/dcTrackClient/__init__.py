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
