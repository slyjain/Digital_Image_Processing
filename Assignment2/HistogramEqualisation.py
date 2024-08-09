from ImageActions import ImageReadColor,ImageSaveGray,ImageReadUnequalisedGray,ImageSaveEqualised
from grayImage import grayImageGenerator
from EqualisationModule import returnEqualisedImage
import numpy as np
image =ImageReadColor()
imageArray=np.array(image)
grayImage=grayImageGenerator(imageArray)
ImageSaveGray(grayImage)

equalisedImage=returnEqualisedImage(grayImage)
ImageSaveEqualised(equalisedImage)
