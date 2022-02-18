class Mystr:
 def __init__(self):
  self.name=""
 
 def get_String(self):
  self.name=input()
 
 def print_String(self):
  print(self.name.upper())
     

name=Mystr()
name.get_String()
name.print_String()
