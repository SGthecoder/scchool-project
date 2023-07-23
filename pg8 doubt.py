# Function to count the number of vowels, consonants, uppercase, and lowercase characters in a text file
def count_characters(filename):
    vowels = 'AEIOUaeiou'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    uppercase_count = 0
    lowercase_count = 0
    vowel_count = 0
    consonant_count = 0

    with open(sample.txt, 'r') as file:
        text = file.read()

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    print("Number of uppercase characters:", uppercase_count)
    print("Number of lowercase characters:", lowercase_count)
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)

# Main program
filename = "sample.txt"
count_characters(filename)
