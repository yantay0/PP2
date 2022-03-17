import os

path , txt =input() , input()
os.chdir(path)
if os.access(path , os.F_OK ) and os.path.exists(path):
 os.remove(txt)
else : print("DOES NOT EXIST")