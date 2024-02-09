# Using 'for' loop
fibonacci_numbers_for = [0, 1]

for i in range(2, 10):
    next_number = fibonacci_numbers_for[-1] + fibonacci_numbers_for[-2]
    fibonacci_numbers_for.append(next_number)

print("Fibonacci numbers using 'for' loop:", fibonacci_numbers_for)
