import cv2
import numpy as np
my_image=cv2.imread("./passport.jpg")
imageArray=np.array(my_image)
height=imageArray.shape[0]
width=imageArray.shape[1]
grayimage=np.zeros((height,width),dtype=np.uint8)
for i in range(height):
    for j in range(width):
        grayimage[i][j]=imageArray[i][j][0]/3
        grayimage[i][j]=grayimage[i][j]+imageArray[i][j][1]/3
        grayimage[i][j]=grayimage[i][j]+imageArray[i][j][2]/3
cv2.imwrite("Gray.jpg",grayimage);
xorer=np.zeros((height,width),dtype=np.uint8)
for i in range(height):
    for j in range(80,180):
        xorer[i][j]=255
for i in range(height):
    for j in range(width):
        grayimage[i][j]=grayimage[i][j]^xorer[i][j]
cv2.imwrite("output.jpg",grayimage)