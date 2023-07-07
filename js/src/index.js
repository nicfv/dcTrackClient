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
     * Generate and return an API token.
     */
    async generateToken() {
        if (this.#username && this.#password && !this.#apiToken) {
            return (await fetch(this.#base_url + '/api/v2/authentication/login', { method: 'POST', headers: [['Authorization', 'Basic ' + btoa(this.#username + ':' + this.#password)]] })).headers.get('Authorization').split(' ')[1];
        } else {
            throw new Error('Username/password undefined or token predefined.');
        }
    }

    /**
     * @private Internal class method.
     */
    async request(method = '', endpoint = '', body = undefined) {
        if (!this.#apiToken) {
            this.#apiToken = await this.generateToken();
        }
        return (await fetch(this.#base_url + '/' + endpoint, { method: method, headers: [['Authorization', 'Bearer ' + this.#apiToken], ['Content-Type', 'application/json']], body: JSON.stringify(body) })).json();
    }
}
