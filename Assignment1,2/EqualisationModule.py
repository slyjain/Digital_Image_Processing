import numpy as np
import sys
import matplotlib.pyplot as plt
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

    plt.figure(figsize=(10, 6))  
    plt.bar(range(256), freq, color='gray') 
    plt.xlabel('Intensity Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Intensity Values For unequalised Image')
    plt.savefig('./plots/histogram.png') 
    
    for i in range(1, 256):
        freq[i] += freq[i - 1]

    
    cdfmin = min(freq[i] for i in range(256) if freq[i] > 0)

    equalisedFreq=np.zeros(256,dtype=np.uint8)
    equalisedImage = np.zeros((rows, cols), dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            equalisedImage[i][j] = round((255 / (rows * cols - cdfmin)) * (freq[tempArray[i][j]] - cdfmin))
            equalisedFreq[equalisedImage[i][j]]=equalisedFreq[equalisedImage[i][j]]+1

    plt.figure(figsize=(10, 6))  
    plt.bar(range(256), equalisedFreq, color='gray') 
    plt.xlabel('Intensity Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Intensity Values For Equalised Image')
    plt.savefig('./plots/equalisedHistogram.png') 
    
    return equalisedImage




# Plot the frequency array
 # Save as PNG file
# plt.savefig('histogram.pdf')  # Save as PDF file
# plt.savefig('histogram.jpg', quality=95)  # Save as JPEG with quality setting

# Display the plot (optional)
# plt.show()
