size = int(input())
a = []
for i in range(0, size):
 a.append(int(input()))

for i in range(0, size):
  if a[i] <= 10 : print("Go to work!")
  if  10 < a[i] <=25 : print("You are weak")
  if 25 < a[i] <= 45 : print("Okay, fine")
  if a[i] > 45 :  print("Burn! Burn! Burn Young!")


