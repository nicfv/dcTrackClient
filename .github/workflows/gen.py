import jsonschema
import json
import re

with open('api.json') as f:
    api = json.load(f)

with open(api['$schema']) as f:
    schema = json.load(f)

try:
    jsonschema.validate(api, schema)
except Exception as e:
    print(e.message)
    exit(1)


def getMethod(transaction: str) -> str:
    if transaction.startswith('get'):
        return 'GET'
    if transaction.startswith('create') or transaction.startswith('search') or transaction.startswith('remove') or transaction.startswith('retrieve'):
        return 'POST'
    if transaction.startswith('update') or transaction.startswith('complete'):
        return 'PUT'
    if transaction.startswith('modify'):
        return 'PATCH'
    if transaction.startswith('delete'):
        return 'DELETE'
    raise Exception('Unknown request type for ' + transaction)


def hasPayload(method: str) -> bool:
    return method == 'POST' or method == 'PUT' or method == 'PATCH'


def getPythonType(type: str) -> str:
    if type == 'string':
        return 'str'
    if type == 'number':
        return 'int'
    if type == 'boolean':
        return 'bool'
    if type == 'object':
        return 'dict'
    raise Exception('Unknown type ' + type)


def generateDocumentation(transaction: str, method: str, endpoint: str, description: str, params: list[str], paramtypes: list[str]) -> None:
    MD = '\n## ' + transaction + '(' + ', '.join(params) + ')\n'
    if description:
        MD += '> ' + description + '\n'
    else:
        MD += '> No documentation provided.\n'
    MD += '```\n' + method + ' ' + endpoint
    if hasPayload(method):
        MD += ' ' + params[-1]
    MD += '\n```\n'
    if params:
        MD += '|Parameter|Type|\n|---|---|\n'
    else:
        MD += '*No parameters.*\n'
    for i in range(0, len(params)):
        MD += '|' + params[i] + '|' + paramtypes[i] + '|\n'
    with open('README.md', 'a') as f:
        f.write(MD)


def generatePythonFunction(transaction: str, method: str, endpoint: str, description: str, params: list[str], paramtypes: list[str], a: int, b: int) -> None:
    endpoint = endpoint.replace('{', '\' + str(').replace('}', ') + \'') + '?'
    for i in range(a, b):
        endpoint += params[i] + '=\' + str(' + params[i] + ') + \'&'
    FUNC = '\n    def ' + transaction + '(self'
    for i in range(0, len(params)):
        FUNC += ', ' + params[i] + ': ' + getPythonType(paramtypes[i])
    FUNC += '):\n        """' + description + '"""\n'
    FUNC += '        return self.__request(\'' + method + '\', \'/' + endpoint + '\''
    if hasPayload(method):
        FUNC += ', ' + params[-1]
    FUNC += ')\n'
    with open('py/src/dcTrackClient/__init__.py', 'a') as f:
        f.write(FUNC)


def generateJavaScriptFunction(transaction: str, method: str, endpoint: str, description: str, params: list[str], paramtypes: list[str], a: int, b: int) -> None:
    endpoint = endpoint.replace('{', '\' + ').replace('}', ' + \'') + '?'
    for i in range(a, b):
        endpoint += params[i] + '=\' + ' + params[i] + ' + \'&'
    FUNC = '\n/**\n * ' + description + '\n'
    for i in range(0, len(params)):
        FUNC += ' * @param {' + paramtypes[i] + '} ' + params[i] + '\n'
    FUNC += ' */\nClient.prototype.' + transaction + ' = function (' + ', '.join(params) + ') {\n'
    FUNC += '    return this.request(\'' + method + '\', \'/' + endpoint + '\''
    if hasPayload(method):
        FUNC += ', ' + params[-1]
    FUNC += ');\n}\n'
    with open('js/src/index.js', 'a') as f:
        f.write(FUNC)


for transaction in api:
    if not str(transaction).startswith('$'):
        METHOD = getMethod(transaction)
        ENDPT = str(api[transaction]['endpoint'])
        PARAMS = re.findall('{([^}]+)}', ENDPT)
        NUMPARAMS = len(PARAMS)
        PTYPES = ['string'] * NUMPARAMS
        DESC = api[transaction].get('description') or 'No documentation provided for `' + transaction + '`.'
        QUERY = api[transaction].get('parameters')
        A = len(PARAMS)
        for i in range(0, A):
            if 'id' in str(PARAMS[i]).lower():
                PTYPES[i] = 'number'
        if QUERY:
            PARAMS += QUERY.keys()
            PTYPES += QUERY.values()
        B = len(PARAMS)
        if hasPayload(METHOD):
            PARAMS += ['payload']
            PTYPES += ['object']
        generatePythonFunction(transaction, METHOD, ENDPT, DESC, PARAMS, PTYPES, A, B)
        generateJavaScriptFunction(transaction, METHOD, ENDPT, DESC, PARAMS, PTYPES, A, B)
        generateDocumentation(transaction, METHOD, ENDPT, DESC, PARAMS, PTYPES)
