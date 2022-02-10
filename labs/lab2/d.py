size, m = int(input()), []
for i in range(size):
    for j in range(size):
        if size % 2 != 0:
         print("." if i+j < size-1 else "#", end="")
        else:
            print("#"if i >= j else ".", end="")
    print()
