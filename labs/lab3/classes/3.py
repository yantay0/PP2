class Shape:
 def area(self):
  return 0

'''
class Square(Shape):
 def __init__(self, lenght):
  self.length = lenght

 def area(self):
  return self.length**2
'''



class Rectangle(Shape):
 def __init__(self , lenght , width):
  self.lenght=lenght
  self.width=width
 def computeArea(self) :
  self.area=self.lenght*self.width
  return self.area


s = Rectangle( 3 , 9 )
print(s.computeArea())