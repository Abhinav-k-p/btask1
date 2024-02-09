start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

sum_odd = 0

num = start
while num <= end:
    if num % 2 != 0:
        sum_odd += num
    num += 1

print(f"The sum of odd numbers in the range {start} to {end} is: {sum_odd}")
