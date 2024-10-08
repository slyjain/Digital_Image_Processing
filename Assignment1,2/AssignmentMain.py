from ImageActions import ImageReadColor,ImageSaveGray,ImageReadUnequalisedGray,ImageSaveEqualised,ImageSaveBlue,ImageSaveGreen,ImageSaveRed
from ColorChanger import grayImageGenerator,redImageGenerator,blueImageGenerator,greenImageGenerator
from EqualisationModule import returnEqualisedImage
import numpy as np
image =ImageReadColor()
imageArray=np.array(image)
grayImage=grayImageGenerator(imageArray)
ImageSaveGray(grayImage)
redImage=redImageGenerator(imageArray)
ImageSaveRed(redImage)
blueImage=blueImageGenerator(imageArray)
ImageSaveBlue(blueImage)
greenImage=greenImageGenerator(imageArray)
ImageSaveGreen(greenImage)
equalisedImage=returnEqualisedImage(grayImage)
ImageSaveEqualised(equalisedImage)
