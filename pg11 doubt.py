# Function to filter lines and write to a new file
def remove_lines_with_character(input_filename, output_filename, character):
    with open(input1.txt, 'r') as infile, open(output1.txt, 'w') as outfile:
        for line in infile:
            if character not in line:
                outfile.write(line)

# Main program
input_file = 'input1.txt'  # Replace with the path to your input file
output_file = 'output1.txt'  # Replace with the path to your output file
character_to_remove = 'a'
remove_lines_with_character(input_file, output_file, character_to_remove)
