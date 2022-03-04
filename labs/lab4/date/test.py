n = int(input())


def gen(n):
 a = 1
 while a <= n:
  yield a**2
  a += 1


print(list(gen(n)))
