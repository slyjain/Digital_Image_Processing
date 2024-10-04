!pip install PyWavelets

import cv2
import pywt
import matplotlib.pyplot as plt

image = cv2.imread('/content/lena.png', cv2.IMREAD_GRAYSCALE)

coeffs2 = pywt.dwt2(image, 'haar')
cA, (cH, cV, cD) = coeffs2

fig, axarr = plt.subplots(2, 2, figsize=(10, 10))

axarr[0, 0].imshow(cA, cmap='gray')
axarr[0, 0].set_title('Approximation')

axarr[0, 1].imshow(cH, cmap='gray')
axarr[0, 1].set_title('Horizontal Detail')

axarr[1, 0].imshow(cV, cmap='gray')
axarr[1, 0].set_title('Vertical Detail')

axarr[1, 1].imshow(cD, cmap='gray')
axarr[1, 1].set_title('Diagonal Detail')

plt.show()
