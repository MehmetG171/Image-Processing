# Define a function to find the index of a value in a list
def index(somelist, value):
    i = 0  # Initialize index
    for c in somelist:
        if c == value:
            return i  # Return index if value found
        i += 1
    return None  # Return None if value not found

gettysburg = ['four', 'score', 'and', 'seven', 'years', 'ago']

# Find and print the index of 'and' in gettysburg list
print(index(gettysburg, 'and'))

# Find and print the index of 'years' in gettysburg list
print(index(gettysburg, 'years'))

# Count and print the occurrences of 'seven' in gettysburg list
print(gettysburg.count('seven'))
