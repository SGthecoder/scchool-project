# Function to print the pattern
def print_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# Main program
rows = 5
print("Pattern:")
print_pattern(rows)
