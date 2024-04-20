in_file = "Sentence.txt"  # Input file name

# Open the input file in read mode
myfile = open(in_file)

num_words = 0  # Word count

# Iterate through each line in the file
for line_of_text in myfile:
    # Split each line into a list of words
    word_list = line_of_text.split()
    # Count the words in the current line and add to the total word count
    num_words += len(word_list)

myfile.close()  # Close the file

print("Total words in file:", num_words)
