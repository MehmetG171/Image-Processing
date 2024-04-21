from skimage import io
import pandas as pd

img = io.imread('puppy.jpg')

# Flatten the image pixel values into a DataFrame
df = pd.DataFrame(img.flatten())

# Specify the filepath for the Excel file
filepath = 'pixel_values.xlsx'

# Save the DataFrame to an Excel file without including the index
df.to_excel(filepath, index = False)
