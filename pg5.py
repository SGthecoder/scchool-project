# Function to check if a value exists in a dictionary
def check_value_in_dict(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

# Main program
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
value_to_check = 3
if check_value_in_dict(my_dict, value_to_check):
    print(f"The value {value_to_check} exists in the dictionary.")
else:
    print(f"The value {value_to_check} does not exist in the dictionary.")
