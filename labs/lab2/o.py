numbers={"ZER":"0" , "ONE":"1" , "TWO":"2" , "THR":"3" , "FOU":"4" , "FIV":"5", "SIX":"6", "SEV":"7", "EIG":"8" , "NIN":"9"}
words={"9":"NIN" , "8":"EIG" , "7":"SEV" , "6":"SIX" , "5":"FIV" , "4":"FOU" , "3":"THR" , "2":"TWO" , "1":"ONE" , "0":"ZER"}

def to_int(s , start, size):
 num=""
 digit=""
 for  i in range (start , size):
  num+=s[i]
  if len(num)==3:
     digit+=numbers[num]
     num=""
 return digit

def to_string(summ):
 word=""
 for i  in summ:
  word+=words[i]
 print(word)

s1=input()
to_string(str(int((to_int(s1, 0, s1.index("+"))))+int(to_int( s1 , s1.index("+")+1 , len(s1)))))






