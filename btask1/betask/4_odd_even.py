test = input("Enter a number: ")

if test.isdigit():
    num = int(test)
    
    if num % 2 == 0:
        print("even number.")
    else:
        print("odd number.")
else:
    print("Invalid input")