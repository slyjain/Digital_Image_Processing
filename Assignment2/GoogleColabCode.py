import cv2

# from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
# Read the image from the specified path
img = cv2.imread('Sonam.png')
cv2.imshow(img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2_imshow(img)

hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
img_hist=cv2.equalizeHist(img)
cv2_imshow(img_hist)
hist=cv2.calcHist([img_hist],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()