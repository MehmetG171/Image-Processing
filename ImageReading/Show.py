from skimage import io

# Read the image 'puppy.jpg' into the img variable
img = io.imread('puppy.jpg')

# Display the image using skimage's imshow function
io.imshow(img)
