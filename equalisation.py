import numpy as np


unequalisedImage = [
    [52, 55, 61, 59, 79, 61, 76, 61],
    [62, 59, 55, 104, 94, 85, 59, 71],
    [63, 65, 66, 113, 144, 104, 63, 72],
    [64, 70, 70, 126, 154, 109, 71, 69],
    [67, 73, 68, 106, 122, 88, 68, 68],
    [68, 79, 60, 70, 77, 66, 58, 75],
    [69, 85, 64, 58, 55, 61, 65, 83],
    [70, 87, 69, 68, 65, 73, 78, 90]
]


arr = np.array(unequalisedImage)


print(arr)
sorter=[]
for i in range(8):
  for j in range(8):
    sorter.append(arr[i][j]);
# print(sorter)
sorter.sort()
# print(sorter)
freq=np.zeros(256);
for i,val in enumerate(sorter):
  freq[val]+=1
# print(freq);
for i in range(256):
  if i>0:
    freq[i]+=freq[i-1]
# print(freq)
import sys
INT_MAX = sys.maxsize
cdfmin=INT_MAX
for i in range(256):
  if freq[i]>0:
      cdfmin=min(freq[i],cdfmin)
  
equalisedImage=np.zeros((8,8))
for i in range(8):
  for j in range(8):
    equalisedImage[i][j]=round((255/63)*(freq[arr[i][j]]-cdfmin))
print(equalisedImage)
