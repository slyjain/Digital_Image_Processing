import cv2


def ImageReadColor():
    image = cv2.imread("./input/image.png")
    return image
def ImageSaveGray(image):
    cv2.imwrite("./output/outputGray/grayImage.png",image)
def ImageReadUnequalisedGray():
    image = cv2.imread("./output/outputGray/grayImage.png")
    return image
def ImageSaveRed(image):
    cv2.imwrite("./output/outputRed/RedImage.png",image)
def ImageSaveBlue(image):
    cv2.imwrite("./output/outputBlue/BLueImage.png",image)
def ImageSaveGreen(image):
    cv2.imwrite("./output/outputGreen/GreenImage.png",image)
def ImageSaveEqualised(image):
    cv2.imwrite("./output/outputEqualised/equalisedGrayImage.png",image)
