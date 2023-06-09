# Changelog

## 0.7.0

- Add `Client.generateToken()` function to generate and return an API token
    - All API calls now require an API token
    - If no API token is provided, one will be provisioned automatically
    - Added documentation in `README.md` regarding generating tokens
- Stricter `schema.json`
    - Function names must begin with `get`, `create`, `search`, `remove`, `update`, or `delete`
    - Endpoints cannot start with a slash
    - Descriptions must contain at least 1 character
    - If `parameters` is set, it must contain at least 1 parameter

## 0.6.2

- Add sublocation API endpoints

## 0.6.1

- Add `updateModel` API function

## 0.6.0

- Add location API endpoints
- Minor updates to readme examples (text fixes)
- HTTP method is inferred by the function name (e.g. `getItem()` = GET request)
- Remove `method` from `api.json`
- Show message when no documentation is provided

## 0.5.2

- Added API functions for managing item ports
- Style updates in readme file

## 0.5.1

- Major updates to the example guide in readme file
- Add `Content-Type: application/json` header in the JavaScript library

## 0.5.0

- Generate JavaScript functions
- JavaScript `Client` is now an instance class
- Update installation commands in `README.md` to show version number
- Update JavaScript setup documentation
- Fix regular expressions in JSON schema
    - Function and parameter names must start with a letter, but can have numbers and underscores
- Stricter checking in JSON schema
    - Improved error reporting
- Readme badges are now clickable links

## 0.4.4

- Remove `types.d.ts` from NPM package
- Improve installation documentation in `README.md`

## 0.4.3

- Update badges in `README.md`
- Convert NPM package to module

## 0.4.2

- Copy readme file to NPM package folder

## 0.4.1

- Only publish NPM package if current version is greater
- Simplify `package.json`

## 0.4.0

- First iteration of NPM package
- Use version number from this file