import math 

def distance (c):
 global P_x , P_y 
 return math.sqrt(((c[0])-P_x)**2+ ((c[1])-P_y)**2)  #fucntion for sorting by the sum pairs in array

P_x , P_y = map (int  , input().split())
size= int(input())

pairs = []

for i in range (size):
 a=[]  
 x, y = map(int, input().split())
 a.append(x)
 a.append(y)
 pairs.append(a) #creating array of arrays(pairs)

pairs.sort(key=distance) 

for i in pairs : 
 print(*i)

 #"*"-Unpacking a function using positional argument.
