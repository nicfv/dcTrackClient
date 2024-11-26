# Changelog

## 1.4.0 (dcTrack 9.2.0)

- Update API guide URL for dcTrack 9.2.0
- Update dependencies in GitHub workflow
- Update dependencies (JavaScript)
- Add `proceedOnWarning` parameter for item API
- Support both `PUT` and `PATCH` (experimental) requests for updating models
- Add `searchAuditTrail` endpoint
- Change `submitRequest` to `createRequest`
- Remove deprecated actuals readings API endpoints

## 1.3.2

- Fix another typo in `updateBreaker`
- Return empty object (`{}`) when no response is given

## 1.3.1

- Fix `updateBreaker` arguments
- Change instances of `ID` to `Id` for consistency

## 1.3.0 (dcTrack 9.1.1)

- Update API guide URL for dcTrack 9.1.1
- Update `searchConnectors` API request
- Add API endpoints for managing breakers
- Update dependency versions (JavaScript)
- Fix command for determining latest package version
- Delete `getSublocationTree` (deprecated)
- Add `updateDefaultValue` and `getFieldProperties`

## 1.2.2

- Use repository shorthand in package file (JavaScript)

## 1.2.1

- All dcTrack 9.1.0 users are encouraged to upgrade to this package version
    - Starting in 9.1.0, API endpoints no longer allow a trailing slash
    - API endpoints still allow multiple consecutive slashes inside the endpoint (e.g. `api///v2///models` works)
- Remove trailing slash in all API endpoints

## 1.2.0 (dcTrack 9.1.0)

- Update API functions to match those in dcTrack version 9.1.0
    - Add `getModelsByNameAndMakeID()`
    - Add functions for power port bulk actual readings
    - Remove `deleteTicketAssignment()`
- Update description for `getItem()`
- Rename a few functions
    - Change `searchMakes()` to `getMakesByName()`
    - Change `deleteCustomFields()` to `deleteCustomField()`
- Add link to new dcTrack API guide in `README.md`
- Schema definition no longer allows endpoints ending in a slash

## 1.1.4

- `getModel()` accepts an integer ID and boolean value for returning the used counts

## 1.1.3

- Minor formatting updates in build files

## 1.1.2

- Add `requests[socks]` dependency (Python)
- Improve documentation on using proxies

## 1.1.1

- Upgrade library to use HTTP/HTTPS or SOCKS proxies (JavaScript)
    - Add `socks-proxy-agent` dependency
- Add instructions on how to set up a SOCKS proxy

## 1.1.0

- Add client option to use a proxy
- Add brief documentation on connecting through a proxy

## 1.0.5

- Add `requests` dependency (Python)

## 1.0.4

- Use `draft-07` JSON schema
- Internal function documentation (Python)

## 1.0.3

- Fix bug where some version numbers weren't replaced. Version numbers are only replaced in select files.

## 1.0.2

- Add documentation in class definition containing version number
- Replace instances of `%VERSION%` with the current version number in any file in this project

## 1.0.1

- Changed development status from `Beta` to `Production/Stable` (Python)

## 1.0.0 (dcTrack 9.0.0)

- First full release, no major changes are expected until the next version release of dcTrack
- Added more information in `README.md`

## 0.9.1

- Added all public facing API endpoints for dcTrack
- New API endpoints:
    - Webhooks
    - Relationships
    - Visualizations
    - Projects
    - Part classes
    - Part models
    - Parts & stock

## 0.9.0

- Functions that begin with `retrieve` are `POST` requests
- Added power chain API endpoints
- Added ticket API endpoints
- Added custom fields API endpoints

## 0.8.1

- Add connection API endpoints

## 0.8.0

- Functions that begin with `submit` are `PUT` requests
- Functions that begin with `complete` are `PUT` requests
- Rename `getAllPermissions()` to `getPermissions()` (*all* is implied)
- Add API endpoints for requests and work orders

## 0.7.2

- Add permission API endpoints
- Add lookup list API endpoints

## 0.7.1

- Add location favorites API endpoints
- Add cabinet space API endpoints

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