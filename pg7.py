# Function to modify a list
def modify_list(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2

# Main program
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
modify_list(my_list)
print("Modified list:", my_list)
