import os

prefix = '/Users/tbear03/'
path = input('Enter the directory: ')

path = prefix + path

num_files = 0
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            num_files += 1

print('Directory contains', num_files, 'Files.')
