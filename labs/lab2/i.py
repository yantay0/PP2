from collections import deque
de , b  = deque([]) , []

for i in range (int(input())):
 a = list(map(str, input().split()))
 if a[0] == "1":
  de.append(a[1])
 if len(a) == 1:
   b.append(de[0])
   de.popleft()

print(*b)
