import cv2 as cv
import numpy as np
# zeros((height, width, color chanelSize), dataType)
blank = np.zeros((500, 500, 3), dtype='uint8')

cv.imshow('Blank', blank)

# blank[height1:height2, width1:width2] = 0, 255, 0
blank[100:200, 200:400] = 0, 255, 0

cv.imshow('Green', blank)

cv.waitKey(0)