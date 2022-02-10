s , lst , ok = input() , [] , True

for bracket in s:
    if  bracket == '(' or bracket == '[' or bracket == '{':
        lst.append(bracket)
    elif lst and (bracket == ')' or bracket == ']' or bracket == '}'):
        if bracket == ')' and lst[-1] == '(' or bracket == ']' and lst[-1] == '[' or bracket == '}' and lst[-1] == '{':
            lst.pop()
        else:
            ok = False
            break
if lst:
    ok = False
print("Yes" if ok == True else "No")
