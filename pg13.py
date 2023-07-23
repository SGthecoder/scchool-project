import csv

# Function to create a CSV file and enter user-id and password
def create_csv_file(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user-id', 'password'])

        while True:
            user_id = input("Enter user-id (or type 'exit' to stop): ")
            if user_id.lower() == 'exit':
                break
            password = input("Enter password: ")
            writer.writerow([user_id, password])

# Function to search for password based on user-id
def search_password_by_user_id(filename, user_id):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == user_id:
                return row[1]
        return None

# Main program - Create CSV file
filename = "user_data.csv"
create_csv_file(filename)

# Search for password based on user-id
search_user_id = input("Enter the user-id to search for the password: ")
password = search_password_by_user_id(filename, search_user_id)
if password:
    print("Password:", password)
else:
    print("User-id not found.")
