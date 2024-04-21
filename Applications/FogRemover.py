import cv2

image = cv2.imread("haze.png", cv2.IMREAD_COLOR)

# Converting the RGB image to LAB color space
rgb2lab = cv2.cvtColor(image, cv2.COLOR_RGB2Lab)

# Creating a CLAHE (Contrast Limited Adaptive Histogram Equalization) object
# clipLimit -> Threshold for contrast limiting
# tileGridSize -> Size of grid for histogram equalization
clahe = cv2.createCLAHE(clipLimit=5, tileGridSize=(8, 8))

# Applying CLAHE to each channel of the LAB image separately
rgb2lab[:, :, 0] = clahe.apply(rgb2lab[:, :, 0])  # L channel
rgb2lab[:, :, 1] = clahe.apply(rgb2lab[:, :, 1])  # A channel
rgb2lab[:, :, 2] = clahe.apply(rgb2lab[:, :, 2])  # B channel

# Converting the modified LAB image back to RGB color space
lab2rgb = cv2.cvtColor(rgb2lab, cv2.COLOR_Lab2RGB)

# Displaying the dehazed image using OpenCV
cv2.imshow("dehaze", lab2rgb)

# Waiting for a key press and then closing all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
