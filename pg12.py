import struct

# Function to update marks in the binary file based on roll number
def update_marks(filename, roll_number, new_marks):
    with open(student_data.dat, 'rb+') as file:
        while True:
            record = file.read(36)  # Assuming each record has a fixed size of 36 bytes (4+20+4)
            if not record:
                break
            roll_no, name, marks = struct.unpack('i 20s f', record)
            if roll_no == roll_number:
                file.seek(-4, 1)  # Move the pointer back 4 bytes to overwrite marks
                file.write(struct.pack('f', new_marks))
                print("Marks updated successfully.")
                return
        print("Roll number not found.")

# Main program
filename = "student_data.dat"
roll_no_to_update = int(input("Enter the roll number to update marks: "))
new_marks_value = float(input("Enter the new marks: "))
update_marks(filename, roll_no_to_update, new_marks_value)
