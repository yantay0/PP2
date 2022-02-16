def rev(string):
 # Разделяю строку по пробелу и сохраняю полученный список в переменной с именем words.
 words = string.split() 
 print(*words[::-1])


rev('We are ready')
