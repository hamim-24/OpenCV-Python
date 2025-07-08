import cv2 as cv

img = cv.imread('abc.png')

if img is None:
    print('Image is not found')
    exit()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

cv.waitKey(0)