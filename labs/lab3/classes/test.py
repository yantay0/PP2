'''

def f1(x):
 return x


print(f1(10))


#lambda arguments : expression

f2= lambda x: x

print(f2(10))



square = lambda x: x*x 

print(square(2))


sum = lambda a, b : a+b

print(sum(2 , 3))
'''

a= [ 1, 2 , 3, 4 , 5]
def double_it(x):
 return x*2
'''
#map(functions , itarabe object)
arr=list(map(double_it , a ))
print(arr)
'''
arr=list(map(lambda x: x*2 , a))
print(arr)


