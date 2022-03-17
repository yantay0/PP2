import os
path = input()
os.chdir(path)
dirs = os.listdir(path)

for i in dirs : print(f'<DIR> {i}' if os.path.isdir(i) else f'<FILE> {i}')
