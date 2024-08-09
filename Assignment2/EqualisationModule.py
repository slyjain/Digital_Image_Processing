import numpy as np
import sys

def returnEqualisedImage(UnEqualisedImage):
    rows = len(UnEqualisedImage)
    cols = len(UnEqualisedImage[0])
    tempArray = np.array(UnEqualisedImage,dtype=np.uint8)
    

    sorter = np.zeros(rows*cols,dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            sorter[i*cols+j]=tempArray[i][j]
    
    sorter.sort()

    
    freq = np.zeros(256,dtype=np.int32)
    for val in sorter:
        freq[val] += 1

    
    for i in range(1, 256):
        freq[i] += freq[i - 1]

    
    cdfmin = min(freq[i] for i in range(256) if freq[i] > 0)

    
    equalisedImage = np.zeros((rows, cols), dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            equalisedImage[i][j] = round((255 / (rows * cols - cdfmin)) * (freq[tempArray[i][j]] - cdfmin))

    return equalisedImage
