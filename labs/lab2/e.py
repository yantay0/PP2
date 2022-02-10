def loop(n , x):
 b , xor=[] , int()
 for i in range (n):
  b.append(x+2*i)
  xor^=b[i]
 print(xor)

a=list(map(int , input().split()))
if len(a)==1 :
 b=[]
 x=int(input())
 loop(a[0] ,x) 
else :
 loop(a[0],a[1])