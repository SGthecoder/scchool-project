#a

import struct

# Function to create a new record and add it to the binary file
def Create(filename):
    with open(filename, 'ab') as file:
        Empid = int(input("Enter Empid: "))
        EName = input("Enter EName: ")
        Designation = input("Enter Designation: ")
        record = struct.pack('i 20s 20s', Empid, EName.encode(), Designation.encode())
        file.write(record)

# Main program
filename = "employee.dat"
Create(filename)


#b

import struct

# Function to display records with Empid > 101
def Display(filename):
    with open(filename, 'rb') as file:
        while True:
            record = file.read(48)  # Assuming each record has a fixed size of 48 bytes (4+20+20)
            if not record:
                break
            Empid, EName, Designation = struct.unpack('i 20s 20s', record)
            if Empid > 101:
                print("Empid:", Empid)
                print("EName:", EName.decode().strip('\x00'))
                print("Designation:", Designation.decode().strip('\x00'))

# Main program
filename = "employee.dat"
Display(filename)
