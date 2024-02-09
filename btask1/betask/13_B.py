num_rows = 4

for i in range(num_rows):
   
    for j in range(i + 1):
        print(j + i * (i + 1) // 2, end=" ")
    
    print()
