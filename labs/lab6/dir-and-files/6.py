import os

path=input()
path = path+'\letters(for 6th task)'

if not os.path.exists('letters(for 6th task)'):
 os.makedirs('letters(for 6th task)')

os.chdir(path)

for i in range(65 , 91):
 f=open(chr(i)+'.txt' , 'w')







