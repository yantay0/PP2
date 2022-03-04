from math import ceil , tan , pi

def area_P(a , b):
 return ceil((a*b**2)/4*tan(pi/a))


n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))


print(f"The area of the polygon is: {area_P(n , s)}")
