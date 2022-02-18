class Point():
 def __init__(self , x, y):
  self.x=x
  self.y=y

 def show(self):
  return self.x , self.y

 def move(self , x , y):
  self.x+=x
  self.y+=y
 
 def dist(self  , p):
  x1=p.x-self.x
  y1=p.y-self.y
  return (x1**2+y1**2)**0.5

p1=Point(3,5)
p2=Point(2 ,4)

print(p1.dist(p2))

