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
def intToBitString(value):
    ans=""
    while value:
        ans=ans+str(int(value%2))
        value=int(value/2)
    if len(ans)<8:
        while len(ans)!=8:
            ans=ans+"0"
        
    return ans[::-1]
image=cv2.imread("./input/img.jpg")
imgArray=np.array(image)
colorOrGray=image.shape[2]
answerImg=np.zeros((imgArray.shape[0],imgArray.shape[1]))

if colorOrGray==1:
    for k in range(8):
        for i in range(imgArray.shape[0]):
            for j in range(imgArray.shape[1]):
                temp=intToBitString(imgArray[i][j])
                answerImg[i][j]=int(temp[k])*(1<<k)
        cv2.imwrite("./output/output"+str(k)+".jpg",answerImg)
else:
    for k in range(8):
        for i in range(imgArray.shape[0]):
            for j in range(imgArray.shape[1]):
                temp=intToBitString(bgrPixelToGray(imgArray[i][j]))
                answerImg[i][j]=int(temp[k])*(1<<k)
        cv2.imwrite("./output/output"+str(k)+".jpg",answerImg)

    



