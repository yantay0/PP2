from itertools import permutations

def perm(string):
 for i in list(permutations(string)):
  print(i)


perm('123')
