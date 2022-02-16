import random


def guess():
    cnt=0
    num=random.randint(1 , 20)
    print("Hello! What is your name?")
    name=input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.' , "Take a guess")
    you=int(input())
    if you > num:
         print("Your guess is too high." , "Take a guess")
         you=int(input())
         cnt+=1
    if you < num("Your guess is too low." , "Take a guess" ):
         you=int(input())
         cnt=+1
    if you==num :
        print("Good job, KBTU! You guessed my number in {cnt} guesses!")
    

guess()