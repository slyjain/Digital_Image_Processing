import cv2 as cv 
import numpy as np 

img=cv.imread("./image.png")
grayImage=cv.cvt(img,cv.COLOR_BGR2GRAY)
im2Array=np.array(grayImage)
imArray=im2Array.flatter()
freq=

