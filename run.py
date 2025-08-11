import os
import shutil

for file in os.listdir('.'):
    if '.' not in file:
        continue
    name, ext = file.split('.')
    name = name.lower()
    if ext == 'py':
        if 'a' in name:
            print(f'Moving {file}')
            if 'og' in name:
                shutil.move(file, f'./A/OG/{file.lower()}')
            else:
                shutil.move(file, f'./A/{file.lower()}')
        if 'b' in name:
            print(f'Moving {file}')
            if 'og' in name:
                shutil.move(file, f'./B/OG/{file.lower()}')
            else:
                shutil.move(file, f'./B/{file.lower()}')
        if 'c' in name:
            print(f'Moving {file}')
            if 'og' in name:
                shutil.move(file, f'./C/OG/{file.lower()}')
            else:
                shutil.move(file, f'./C/{file.lower()}')
        if 'd' in name:
            print(f'Moving {file}')
            if 'og' in name:
                shutil.move(file, f'./D/OG/{file.lower()}')
            else:
                shutil.move(file, f'./D/{file.lower()}')