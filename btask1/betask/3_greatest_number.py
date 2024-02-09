num1=input("enter the number:")
num2=input("enter the number:")
num3=input("enter the number:")

if num1 == num2 == num3:
    print("Equal: All three numbers are the same.")
    
else:
    greatest_number = num1

    if num2 > greatest_number:
        greatest_number = num2

    if num3 > greatest_number:
        greatest_number = num3
        
    print(greatest_number)