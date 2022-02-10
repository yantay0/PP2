import math
def prime(x):
  if x > 2 : 
    for i in range (2, int(math.sqrt(x))+1) :
      if x%i==0 :
       return False
  return True

distance , target= map(int , input().split())
print("Good job!" if (target % 2 == 0) and (distance < 500 and (prime(distance) or distance == 3 or distance == 2)) else "Try next time!")
