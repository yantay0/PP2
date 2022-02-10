all = {}

for i in range(int(input())):
 demon, power = input().split()
 if power in all:
  all[power] = int(all[power]+1)
 else:
  all[power] = 1

for i in range(int(input())):
 hunter, tech, num = input().split()
 if tech in all:
  all[tech] =int(all[tech])-int(num)

left = 0

for i in all:
 if all[i] > 0:
  left = left+int(all[i])
print("Demons left: ", left)
