size = int(input())
lst=[]
for i in range (0  , size):
 lst.append(input())

for i in range(0, len(lst)):
 if lst[i][-10:] == "@gmail.com": print(lst[i][:-10])


