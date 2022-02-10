a = []
while (True):
 x = int(input())
 if x == 0:
  break
 a.append(x)
for i in range(0, len(a)//2):
  sum = a[i]+a[len(a) - i - 1]
  print(sum, end=" ")
  sum = 0
if len(a) % 2 == 1:
   print(a[len(a)//2])
