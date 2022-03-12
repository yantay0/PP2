import re

def  first(text):
 x = re.search('a(b*)', text)  # an 'a' followed by zero or more 'b''s.
 return x

def second(text):
 x = re.search('ab{2,3}' , text) #with a folowed by 2 to 3
 return x

def third(text):
 x = re.search('^[a-z]+_[a-z]+$' , text)  #lower case letters with underscope between 
 return x

def forth(text):
 x = re.search('^[A-Z]([a-z]+)' , text) #begins with upper case letter and folowed by lower case letters
 return x

def fifth(text):
 x = re.findall("^a(.*)b$", text)  #string must begin with "a" and end with "b"
 return x


def sixth(text):
 x = re.sub("[, .]",  ":"  ,text) #replace all dots , comma , space by colon
 return x

def seventh(text):
 x = re.sub("_" , "" , text.title()) #convert snake case string to camel
 return x

def eighth(text):
 x = re.findall('[A-Z][a-z]*' , text) #split a string into parts by uppercase capital letter
 return x

def ninth(text):
 x = re.findall('[A-Z][a-z]*', text)# insert space  by uppercase capital letter
 return ' '.join(x)

def tenth(text):
 text = re.findall('[A-Z][a-z]*', text)  # convert camel case string to snake
 return "_".join(text).lower()



#tests

'''
txt = input()

print("Match!" if fifth(txt) else "No match!") #test for 1 to 5

'''
print(sixth("hello , dear friend."))

print(seventh("this_is_snake_case"))

print(eighth("HelloMyNameIsJohn"))

print(ninth("HelloMyNameIsJohn"))

print(tenth("ThisIsSnakeCase"))













