import requests


class Client:
    """Sunbird dcTrack API client version %VERSION% in Python"""

    def __init__(self, baseUrl: str, username: str = '', password: str = '', apiToken: str = ''):
        """Provide either a username and password, or an API token to access the dcTrack database with Python."""
        self.__BASE_URL = baseUrl
        self.__USERNAME = username
        self.__PASSWORD = password
        self.__APITOKEN = apiToken

    def generateToken(self) -> str:
        """Generate and return an API token."""
        if self.__USERNAME and self.__PASSWORD and not self.__APITOKEN:
            return requests.request('POST', self.__BASE_URL + '/api/v2/authentication/login', auth=(self.__USERNAME, self.__PASSWORD)).headers['Authorization'].split()[1]
        else:
            raise Exception('Username/password undefined or token predefined.')

    def __request(self, method: str, endpoint: str, body: dict = None):
        if not self.__APITOKEN:
            self.__APITOKEN = self.generateToken()
        return requests.request(method, self.__BASE_URL + '/' + endpoint, json=body, headers={'Authorization': 'Bearer ' + self.__APITOKEN}).json()
