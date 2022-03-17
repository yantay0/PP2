import os 
path = input()
os.chdir(path)


if os.path.exists(path) :
 dirs =os.listdir(path)

 for file in dirs : 
  if os.path.isfile(file):  print( f'Directory portion: {os.path.dirname(path)} <FILE> {file}')
else : "DOES NOT EXIST" 