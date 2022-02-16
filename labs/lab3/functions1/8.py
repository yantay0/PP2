def spy_game(nums , spy=""):
 for x in nums :
  if x==0 or x==7 : spy+=str(x)
 if spy=="007":
  return True
 return False 

print(spy_game([1,2,4,0,0,7,5]) )
print(spy_game([1,0,2,4,0,5,7]) )
print(spy_game([1,7,2,0,4,5,0]) )