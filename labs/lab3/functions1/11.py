def palindrome(word):
 if type(word)==str: word=word.split()  
 s=word[::-1]
 if s==word:
  return True
 return False 

print("yes" if palindrome([1 , 2, 2, 3,1]) else "no")
