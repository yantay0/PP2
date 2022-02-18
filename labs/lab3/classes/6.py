a=[ 1,12 , 2  , 3  , 103 , 97 , 25 , 50]

primes=list(filter(lambda x : all(x%i!=0 for i in range ( 2 , x)) and x!=1 , a))

print(primes)