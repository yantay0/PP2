s , up , low=input()  , 0 , 0

for i in s : 
 if 65 <= ord(i) <= 90 : up+=1
 elif 97 <= ord(i) <= 122 : low+=1

print(f"uppercase: {up}\nlowercase: {low}") 



