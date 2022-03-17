import os 
path  , txt1 , txt2 =input() , input() , input()
os.chdir(path)
with open ( txt1 , 'r') as f1 , open (txt2 , 'w') as f2:
 for x in f1 : f2.write(x)

f2=open(txt2)
print(f2.read())