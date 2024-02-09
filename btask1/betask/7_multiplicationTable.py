number = int(input("Enter the number for the multiplication table: "))
end_limit = int(input("Enter the end limit for the table: "))

for i in range(1, end_limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
5