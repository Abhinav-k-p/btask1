# Using 'while' loop
fibonacci_numbers_while = [0, 1]
count = 2

while count < 10:
    next_number = fibonacci_numbers_while[-1] + fibonacci_numbers_while[-2]
    fibonacci_numbers_while.append(next_number)
    count += 1

print("Fibonacci numbers using 'while' loop:", fibonacci_numbers_while)
