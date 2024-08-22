import cv2
import numpy as np

# Read the image
my_image = cv2.imread("./passport.jpg")

# Convert the image to an array
imageArray = np.array(my_image)

# Get the height and width of the image
height = imageArray.shape[0]
width = imageArray.shape[1]

# Initialize an empty grayscale image array with the same shape and type as the original image
grayimage = np.zeros((height, width), dtype=np.uint8)

# Convert to grayscale
for i in range(height):
    for j in range(width):
        grayimage[i][j] = imageArray[i][j][0] / 3 + imageArray[i][j][1] / 3 + imageArray[i][j][2] / 3

# Initialize the XOR mask
xorer = np.zeros((height, width), dtype=np.uint8)
for i in range(height):
    for j in range(80, 180):
        xorer[i][j] = 255

# Apply XOR operation
for i in range(height):
    for j in range(width):
        grayimage[i][j] = np.uint8(grayimage[i][j]) ^ xorer[i][j]

# Save the processed image
cv2.imwrite("output.jpg", grayimage)
