from skimage.io import imread
from skimage import color
import matplotlib.pyplot as plt

original = imread('image.jpg')

# Convert the image to grayscale
grayscale = color.rgb2gray(original)

# Define a function to display the image
def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Show the grayscale image
show_image(grayscale, 'Grayscale')

# Extract the red, green, and blue channels from the original image
red = original[:, :, 0]
green = original[:, :, 1]
blue = original[:, :, 2]

# Define a function to display grayscale images
def show_grayscale(image, title):
    plt.imshow(image, cmap="gray") 
    plt.title(title)
    plt.axis('off')
    plt.show()

# Display the Red channel in grayscale
show_grayscale(red, 'Red Grayscale')

# Display the Green channel in grayscale
show_grayscale(green, 'Green Grayscale')

# Display the Blue channel in grayscale
show_grayscale(blue, 'Blue Grayscale')

def plot_histogram(image_channel, color):
    # Plot the histogram for the given image channel with bins in a range of 256
    plt.hist(image_channel.ravel(), bins=256, color=color)
    plt.title(f'{color.capitalize()} Histogram') 
    plt.xlabel('Pixel Value') 
    plt.ylabel('Frequency')
    plt.show() 

# Plot the red histogram
plot_histogram(red, 'red')

# Plot the green histogram
plot_histogram(green, 'green')

# Plot the blue histogram
plot_histogram(blue, 'blue')
