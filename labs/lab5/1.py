import re 

x= re.search('a(b*)$ ' , 'row.txt')
print("yes" if x else "no")

