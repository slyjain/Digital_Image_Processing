import cv2
import numpy as np
imgBGR=cv2.imread('image.jpg')
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

def lbp(i,j,array,narray):
    m=1
    value=0
    for k in range(8):
        xx=array[i+dx[k]][j+dy[k]]>=array[i][j]
        value+=m*xx
        m=m*2
    lbpArray[i][j]=value
    



imgGray=cv2.cvtColor(imgBGR,cv2.COLOR_BGR2GRAY)
imageArray=np.array(imgGray)
height=len(imageArray)

width=len(imageArray[0])
lbpArray=np.zeros((height,width),dtype=np.uint8)
for i in range(1,height-1):
    for j in range(1,width-1):
       lbp(i,j,imageArray,lbpArray)
lbpArray[0, :] = imageArray[0, :]  # First row
lbpArray[-1, :] = imageArray[-1, :]  # Last row
lbpArray[:, 0] = imageArray[:, 0]  # First column
lbpArray[:, -1] = imageArray[:, -1]
# cv2.imshow('LBP Image', lbpArray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('lbp.jpg',lbpArray)