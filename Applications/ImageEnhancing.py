import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from skimage.io import imread
import cv2

original = imread('deneme.tiff')

# Obtain the red, green, and blue values of the image
red = original[:, :, 0]
green = original[:, :, 1]
blue = original[:, :, 2]

# Display Red, Green, and Blue grayscale images
plt.imshow(red, cmap="gray")
plt.title('Red Grayscale')
plt.axis('off')
plt.show()

plt.imshow(green, cmap="gray")
plt.title('Green Grayscale')
plt.axis('off')
plt.show()

plt.imshow(blue, cmap="gray")
plt.title('Blue Grayscale')
plt.axis('off')
plt.show()

# Plot the histograms for Red, Green, and Blue channels
plt.hist(red.ravel(), bins=256, color='red')
plt.title('Red Histogram')
plt.show()

plt.hist(green.ravel(), bins=256, color='green')
plt.title('Green Histogram')
plt.show()

plt.hist(blue.ravel(), bins=256, color='blue')
plt.title('Blue Histogram')
plt.show()

# Load the image again using OpenCV for further processing
img = cv.imread('deneme.tiff', cv.IMREAD_GRAYSCALE)
assert img is not None, "File could not be read."

# Plot the histogram and cumulative distribution function (CDF)
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('CDF', 'Histogram'), loc='upper left')
plt.show()

# Apply histogram equalization using OpenCV
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))  # Stacking images side-by-side

# Save the result
cv.imwrite('res.png', res)

# Perform histogram equalization separately for each channel (R, G, B) using OpenCV
image_src = cv2.imread('deneme.tiff')
image_src = cv2.cvtColor(image_src, cv2.COLOR_BGR2RGB)
r_image, g_image, b_image = cv2.split(image_src)
r_image_eq = cv2.equalizeHist(r_image)
g_image_eq = cv2.equalizeHist(g_image)
b_image_eq = cv2.equalizeHist(b_image)
image_eq = cv2.merge((r_image_eq, g_image_eq, b_image_eq))

# Display the original and equalized images side by side
fig = plt.figure(figsize=(10, 20))
ax1 = fig.add_subplot(2, 2, 1)
ax1.axis("off")
ax1.title.set_text('Original')
ax2 = fig.add_subplot(2, 2, 2)
ax2.axis("off")
ax2.title.set_text("Equalized")
ax1.imshow(image_src)
ax2.imshow(image_eq)
plt.show()

# Apply Contrast Limited Adaptive Histogram Equalization (CLAHE) using OpenCV
clahe = cv.createCLAHE(clipLimit=3, tileGridSize=(8, 8))
cl = clahe.apply(img)

# Save the result of CLAHE
cv.imwrite('clahe.jpg', cl)
