matrix = []

# Iterate through rows
for i in range(5):
    row = []  # Initialize an empty row for each iteration of i
    # Iterate through columns
    for j in range(5):
        row.append(i + j)  # Add the sum of i and j to the current row
    matrix.append(row)  # Add the completed row to the matrix

print(matrix)
