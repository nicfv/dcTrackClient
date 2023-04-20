
with open('src/dcTrackClient/__init__.py') as f:
    content = f.read()

print('## Module Documentation')

for line in content.split('\n'):
    line = line.strip()
    if line.startswith('class'):
        print('### ' + line)
    elif line.startswith('def') and not line.startswith('def __') or line.startswith('def __init__'):
        print('```py')
        print(line)
        print('```')
    elif line.startswith('"""'):
        print('> ' + line.strip('"""'))
