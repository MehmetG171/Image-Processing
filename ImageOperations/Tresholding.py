from skimage.filters import threshold_local, threshold_otsu, try_all_threshold
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import color
import cv2

# Define a function to display the image
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

original = imread('image.jpg')

grayscale = color.rgb2gray(original)

block_size = 351

# Obtain the optimal local thresholding
local_thresh = threshold_local(grayscale, block_size, offset=0.1)

# Obtain the binary image by applying local thresholding
binary_local = grayscale > local_thresh

# Show the binary image for local thresholding
show_image(binary_local, 'Local Thresholding')

# Obtain the optimal Otsu global threshold value
global_thresh = threshold_otsu(grayscale)

# Obtain the binary image by applying global thresholding
binary_global = grayscale > global_thresh

# Show the binary image for global thresholding
show_image(binary_global, 'Global Thresholding')

# Use the try all method on the resulting grayscale image to explore multiple thresholding techniques
fig, ax = try_all_threshold(grayscale, verbose=False)

plt.show() 

img = cv2.imread('image.jpg', 0)

# Apply global thresholding
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Apply adaptive thresholding with MEAN_C method
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)

# Apply adaptive thresholding with GAUSSIAN_C method
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 11, 2)

# Display the original image and thresholded images
plt.subplot(221), plt.imshow(img, 'gray')
plt.title('Original Image')

plt.subplot(222), plt.imshow(thresh1, 'gray')
plt.title('THRESH_BINARY')

plt.subplot(223), plt.imshow(thresh2, 'gray')
plt.title('ADAPTIVE_THRESH_MEAN_C')

plt.subplot(224), plt.imshow(thresh3, 'gray')
plt.title('ADAPTIVE_THRESH_GAUSSIAN_C')

plt.show()
