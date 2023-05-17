class Client {
    static #base_url;
    static #username;
    static #password;
    static #apiToken;
    /**
     * Provide either a username and password, or an API token to access the dcTrack database with JavaScript.
     */
    static authenticate(base_url = '', credentials = { username: '', password: '', apiToken: '' }) {
        this.#base_url = base_url;
        this.#username = credentials.username;
        this.#password = credentials.password;
        this.#apiToken = credentials.apiToken;
    }

    static async request(method = '', endpoint = '', body = undefined) {
        let authHeader = '';
        if (this.#username && this.#password) {
            authHeader = 'Basic ' + btoa(this.#username + ':' + this.#password);
        } else if (this.#apiToken) {
            authHeader = 'Token ' + this.#apiToken;
        } else {
            throw new Error('Undefined username/password or token.');
        }
        return (await fetch(this.#base_url + '/' + endpoint, { 'method': method, 'headers': [['Authorization', authHeader]], 'body': JSON.stringify(body) })).json();
    }
}
