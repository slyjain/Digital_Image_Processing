import cv2;
import numpy as np
def threshold(value):
    return 255 if value>127 else 0
def bgrPixelToGray(arr):
    ans=0
    for i in range(3):
        ans=ans+arr[i]
    ans=ans/3
    return ans
image=cv2.imread("./input/img.jpg")
imgArray=np.array(image)
colorOrGray=image.shape[2]
answerImg=np.zeros((imgArray.shape[0],imgArray.shape[1]))
if colorOrGray==1:
    for i in range(imgArray.shape[0]):
        for j in range(imgArray.shape[1]):
            answerImg[i][j]=threshold(imgArray[i][j])
else:
    for i in range(imgArray.shape[0]):
        for j in range(imgArray.shape[1]):
            answerImg[i][j]=threshold(bgrPixelToGray(imgArray[i][j]))
cv2.imwrite("./output/output.jpg",answerImg)

