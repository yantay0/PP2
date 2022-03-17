l=['hello' , 'my' , 'name']
txt=input()
with open (txt , 'w') as f: 
 f.write('\n'.join(l))
f=open(txt)
print(f.read())
f.close()

