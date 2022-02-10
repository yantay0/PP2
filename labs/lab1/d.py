n=int(input())
z=input()
print(round(n/1024, int(input())) if z == "k" else n*1024)

