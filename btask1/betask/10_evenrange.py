start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

sum_even = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        sum_even += num

print(f"The sum of even numbers in the range {start} to {end} is: {sum_even}")
