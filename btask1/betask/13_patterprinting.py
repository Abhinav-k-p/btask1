num_rows = 4

for i in range(1, num_rows + 1):
   
    for j in range(num_rows - i):
        print(" ", end="")

    for k in range(i):
        print("* ", end="")

    print()
