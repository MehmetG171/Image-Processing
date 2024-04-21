import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('moliets.png')

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for blue color in HSV
lower_blue = np.array([75, 50, 50])
upper_blue = np.array([135, 255, 255])

# Create a mask based on the blue color range
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply Morphological Transformations (opening and closing) to the mask
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

# Find contours in the processed image
contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the original image for drawing contours
img_contours = np.copy(img)
cv2.drawContours(img_contours, contours, -1, (0, 0, 255), 3)

# Plotting the figures using matplotlib
fig, axs = plt.subplots(3, 1, figsize=[15, 15])
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title("Original Image")
axs[1].imshow(closing, cmap="gray")
axs[1].set_title("Masked Image")
axs[2].imshow(cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB))
axs[2].set_title("Number of Pools = {}".format(len(contours)))

plt.show()
