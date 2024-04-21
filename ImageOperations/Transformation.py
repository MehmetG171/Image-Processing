from skimage.io import imread
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from skimage.color import rgb2hsv
from skimage.color import rgb2gray
from skimage.util import img_as_uint
import numpy as np

pic = imread('image.jpg')
imshow(pic)

# Create subplots for the split images
fig, ax = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

# Show the splits
ax[0].imshow(pic[:, 0:250])
ax[0].set_title('First Split')

ax[1].imshow(pic[:, 250:500])
ax[1].set_title('Second Split')

ax[2].imshow(pic[:, 500:750])
ax[2].set_title('Third Split')

plt.show()

# Display a zoomed-in portion of the image
plt.imshow(pic[350:550, 250:350])

# Create subplots for displaying RGB channels
fig, ax = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

# Display the Red channel
ax[0].imshow(pic[:, :, 0], cmap='Reds')
ax[0].set_title('Red')

# Display the Green channel
ax[1].imshow(pic[:, :, 1], cmap='Greens')
ax[1].set_title('Green')

# Display the Blue channel
ax[2].imshow(pic[:, :, 2], cmap='Blues')
ax[2].set_title('Blue')

plt.show()

# Convert the image to HSV color space
pic_hsv = rgb2hsv(pic)

# Create subplots for displaying HSV channels
fig, ax = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

# Display the Hue channel
ax[0].imshow(pic_hsv[:, :, 0], cmap='hsv')
ax[0].set_title('Hue')

# Display the Saturation channel
ax[1].imshow(pic_hsv[:, :, 1], cmap='gray')
ax[1].set_title('Saturation')

# Display the Value channel
ax[2].imshow(pic_hsv[:, :, 2], cmap='gray')
ax[2].set_title('Value')

plt.show()

# Convert the image to grayscale
pic_gray = rgb2gray(pic)

# Create subplots for displaying grayscale variations
fig, ax = plt.subplots(1, 5, figsize=(17, 6), sharey=True)

# Display the original grayscale image
ax[0].imshow(pic_gray, cmap='gray')
ax[0].set_title('Grayscale Original')

# Display pixels greater than 0.25 in grayscale
ax[1].imshow(img_as_uint(pic_gray > 0.25), cmap='gray')
ax[1].set_title('Greater than 0.25')

# Display pixels greater than 0.50 in grayscale
ax[2].imshow(img_as_uint(pic_gray > 0.50), cmap='gray')
ax[2].set_title('Greater than 0.50')

# Display pixels greater than 0.75 in grayscale
ax[3].imshow(img_as_uint(pic_gray > 0.75), cmap='gray')
ax[3].set_title('Greater than 0.75')

# Display pixels greater than the mean in grayscale
ax[4].imshow(img_as_uint(pic_gray > np.mean(pic_gray)), cmap='gray')
ax[4].set_title('Greater than Mean')

plt.show()
