from skimage import io, color
from pylab import *

img = io.imread('puppy.jpg')

# Convert the image to HSV color space
img_hsv = color.rgb2hsv(img)

# Convert the HSV image back to RGB
img_rgb = color.hsv2rgb(img_hsv)

# Show the HSV image
figure(0)
io.imshow(img_hsv)

# Show the RGB image
figure(1)
io.imshow(img_rgb)
