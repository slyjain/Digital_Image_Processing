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