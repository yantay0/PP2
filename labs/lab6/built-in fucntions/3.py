s , cnt  =input()  , 0 
t = reversed(s)
for i in s : 
 if i==next(t): cnt+=1
print("It's Palindrome!" if cnt==len(s) else "It's not Palindrome" )


