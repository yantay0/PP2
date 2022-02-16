def unique(arr):
 new=[]
 for x in arr:
  if x not in new : new.append(x)
 return new

print(unique([1 , 2, 2, 3, 4]))