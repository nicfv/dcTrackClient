import requests


class Client:
    """Sunbird dcTrack API client version %VERSION% in Python"""

    def __init__(self, baseUrl: str, username: str = '', password: str = '', apiToken: str = '', httpProxy: str = '', httpsProxy: str = ''):
        """Provide either a username and password, or an API token to access the dcTrack database with Python."""
        self.__BASE_URL = baseUrl
        self.__USERNAME = username
        self.__PASSWORD = password
        self.__APITOKEN = apiToken
        self.__PROXY = {}
        if httpProxy:
            self.__PROXY['http'] = httpProxy
        if httpsProxy:
            self.__PROXY['https'] = httpsProxy

    def generateToken(self) -> str:
        """Generate and return an API token."""
        if self.__USERNAME and self.__PASSWORD and not self.__APITOKEN:
            return requests.request('POST', self.__BASE_URL + '/api/v2/authentication/login', auth=(self.__USERNAME, self.__PASSWORD), proxies=self.__PROXY).headers['Authorization'].split()[1]
        else:
            raise Exception('Username/password undefined or token predefined.')

    def __request(self, method: str, endpoint: str, body: dict = None):
        """Internal class method."""
        if not self.__APITOKEN:
            self.__APITOKEN = self.generateToken()
        response = requests.request(method, self.__BASE_URL + '/' + endpoint, json=body, headers={'Authorization': 'Bearer ' + self.__APITOKEN}, proxies=self.__PROXY)
        try:
            return response.json()
        except:
            return {}
