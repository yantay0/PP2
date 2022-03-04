n = int(input())


def gen(n):
 a = 0
 while a <= n:
  if a%2==0 : yield a
  a += 1


print(list(gen(n)))
