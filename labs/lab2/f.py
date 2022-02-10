n = int(input())
student = {}  # creating a dictionary

for i in range(n):
 name, money = input().split()
 if name in student:
  # if name already in dict we will sum the value with next money else we do not summarize
  student[name] = int(student[name])+int(money)
 else:
  student[name] = int(money)

overall = (sorted(student.keys()))
max = max(student.values())  # the maxi amount

for i in overall:
 if student[i] == max:
  print(i, " is lucky!")
 else:
  print(i, " has to receive ", max - int(student[i]), " tenge")
