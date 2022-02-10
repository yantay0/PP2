n = int(input())
a=[]
for i in range (n):
  s=input()
  mixed_case = not s.islower() and not s.isupper()
  if (mixed_case):
   for x in "0123456789":
    if x in s:
     a.append(s)

p=set(a)
a=list(sorted(p))
print(len(a))
for x in a:
 print(x)

