import numpy as np
import matplotlib.pyplot as plt

# Define a 2x2 matrix
array_1 = np.array([[255, 0],
                    [0, 255]])

# Display the matrix as an image with grayscale colormap
plt.imshow(array_1, cmap='gray')

# Define a 3x3 matrix
array_2 = np.array([[255, 0, 255],
                    [0, 255, 0],
                    [255, 0, 255]])

# Display the matrix as an image with grayscale colormap
plt.imshow(array_2, cmap='gray')

# Using arange function and its transpose
array_spectrum = np.array([np.arange(0, 255, 17),
                           np.arange(255, 0, -17),
                           np.arange(0, 255, 17),
                           np.arange(255, 0, -17)])

# Create subplots with 1 row and 2 columns, setting the figure size
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

# Plot the original array
ax[0].imshow(array_spectrum, cmap='gray')
ax[0].set_title('Arange Generation') 

# Plot the transposed array
ax[1].imshow(array_spectrum.T, cmap='gray')
ax[1].set_title('Transpose Generation') 

# Creating a 1x3 matrix with colors
array_colors = np.array([[[255, 0, 0],  # Red
                          [0, 255, 0],  # Green
                          [0, 0, 255]]])  # Blue

plt.imshow(array_colors);
