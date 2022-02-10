size, m = int(input()), []

for i in range(size):
    for j in range(size):
        if i == 0:
         print(j, sep=" ", end=" ")
        elif j == 0:
         print(i, sep=" ",  end=" ")
        elif i == j:
         print(i*j, sep=" ", end=" ")
        else:
         print(0, sep=" ", end=" ")
    print()
