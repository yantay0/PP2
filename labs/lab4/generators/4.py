def squares(a, b):
 for i in range(a, b):
  yield i*i

  
a, b = int(input()), int(input())





print(list(squares(a , b)))


