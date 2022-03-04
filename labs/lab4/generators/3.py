n = int(input())


def div(n):
  for i in range (0 , n):
   if i%3==0 and i%4==0 : yield i


print(list(div(n)))
