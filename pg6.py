# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Main program
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate: "))
time_period = float(input("Enter the time period (in years): "))

interest_amount = calculate_simple_interest(principal_amount, interest_rate, time_period)
print("Simple Interest:", interest_amount)
