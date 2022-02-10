dates=[]
while(True):
 a=list((map(str, input().split())))
 if len(a)==1: 
  break
 dates.append(a[::-1])
sort_cal=sorted(dates)
for i in range (len(sort_cal)):
 print(*sort_cal[i][::-1])