# Initialize sum to 0
sum_even = 0

# Iterate through numbers 1 to 7
for num in range(1, 8):
    if num % 2 == 0:
        sum_even += num

print("Sum of even numbers from 1 to 7:", sum_even)
