# Function to read a text file and display each word separated by a #
def display_words_with_separator(filename):
    with open(textfile.txt, 'r') as file:
        for line in file:
            words = line.strip().split()
            print("#".join(words))

# Main program
filename = "textfile.txt"  # Replace with the path to your text file
display_words_with_separator(filename)
