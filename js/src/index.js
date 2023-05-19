export class Client {
    #base_url;
    #username;
    #password;
    #apiToken;
    /**
     * Provide either a username and password, or an API token to access the dcTrack database with JavaScript.
     */
    constructor(base_url = '', credentials = { username: '', password: '', apiToken: '' }) {
        this.#base_url = base_url;
        this.#username = credentials.username;
        this.#password = credentials.password;
        this.#apiToken = credentials.apiToken;
    }

    /**
     * @private Internal class method.
     */
    async request(method = '', endpoint = '', body = undefined) {
        let authHeader = '';
        if (this.#username && this.#password) {
            authHeader = 'Basic ' + btoa(this.#username + ':' + this.#password);
        } else if (this.#apiToken) {
            authHeader = 'Token ' + this.#apiToken;
        } else {
            throw new Error('Undefined username/password or token.');
        }
        return (await fetch(this.#base_url + '/' + endpoint, { method: method, headers: [['Authorization', authHeader], ['Content-Type', 'application/json']], body: JSON.stringify(body) })).json();
    }
}
