import cv2


def ImageReadColor():
    image = cv2.imread("./input/image.png")
    return image
def ImageSaveGray(image):
    cv2.imwrite("./outputGray/grayImage.png",image)
def ImageReadUnequalisedGray():
    image = cv2.imread("./outputGray/grayImage.png")
    return image
def ImageSaveEqualised(image):
    cv2.imwrite("./outputEqualised/equalisedGrayImage.png",image)
