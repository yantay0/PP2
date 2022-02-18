class Account:
 def __init__(self , owner  , balance=0 ):
  self.owner=owner
  self.balance=balance
  

 def deposit(self , in_dep):
  self.balance+=in_dep


 def withdraw(self , out_dep) :
  if out_dep>self.balance:
   print("There are not enough funds in your account")
   return self.balance
  else :
   self.balance-=self.balance-out_dep

 def inf(self):
  return(f'Account owner: {self.owner} \nAccount balance: {self.balance}')



a=Account("Madina")

a.withdraw(1)





