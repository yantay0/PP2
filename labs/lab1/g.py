b = input()
s = b[::-1]
x = 0
for i in range(0, len(s)):
 if s[i] == "1":
  x = x+pow(2, i)
print(x)