from time import sleep

x , s =int(input()) , int(input())

sleep(s/10000)
print(f"Square root of {x} after {s} miliseconds is " ,  pow(x , 0.5  ))
