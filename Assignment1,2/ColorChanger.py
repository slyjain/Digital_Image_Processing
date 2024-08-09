import numpy as np
def grayImageGenerator(imageArray):
    rows=len(imageArray)
    cols=len(imageArray[0])
    answerArray=np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                answerArray[i][j]=imageArray[i][j][k]+answerArray[i][j]
            answerArray[i][j]=answerArray[i][j]/3
    return answerArray
def blueImageGenerator(image):
    imageArray=image.copy()
    rows=len(imageArray)
    cols=len(imageArray[0])
    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                if k==1 or k==2:
                    imageArray[i][j][k]=0
    return imageArray
def greenImageGenerator(image):
    imageArray=image.copy()
    rows=len(imageArray)
    cols=len(imageArray[0])
    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                if k==0 or k==2:
                    imageArray[i][j][k]=0
    return imageArray
def redImageGenerator(image):
    imageArray=image.copy()
    rows=len(imageArray)
    cols=len(imageArray[0])
    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                if k==0 or k==1:
                    imageArray[i][j][k]=0
    return imageArray