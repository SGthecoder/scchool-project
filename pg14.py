# Function to compute the nth Fibonacci number using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input! n should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to compute the nth Fibonacci number using iteration
def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input! n should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Main program
n = int(input("Enter the value of n to find the nth Fibonacci number: "))

# Using recursion
fib_recursive = fibonacci_recursive(n)
print("Using recursion, the nth Fibonacci number is:", fib_recursive)

# Using iteration
fib_iterative = fibonacci_iterative(n)
print("Using iteration, the nth Fibonacci number is:", fib_iterative)
