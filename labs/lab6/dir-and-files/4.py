txt=input() #put your file name
with open (txt , 'r') as f:
 x = len(f.readlines())
 print("Number of lines:" , x)
f.close()