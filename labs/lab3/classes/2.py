class Shape:
 def area(self):
  return 0 
 
class Square(Shape):
 def __init__(self , lenght):
  self.length=lenght
 def area(self):
  return self.length**2

 
s= Square(int(input()))
print(s.area())