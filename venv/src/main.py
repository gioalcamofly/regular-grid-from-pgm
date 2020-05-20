import cv2 as cv
import numpy as nd
import sys

img = cv.imread('/home/giovanni/Escritorio/housemap.pgm')


if img is None:
    sys.exit('Can\'t read image')

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh_img = cv.threshold(gray_img, 240, 255, 0)

contours = cv.findContours(thresh_img, 1, 2)

cnt = contours[0]

x,y,w,h = cv.boundingRect(cnt)
print x
print y
print w
print h

cropped_img = thresh_img[y:(y+h), x:(x+w)]

cv.imshow('Rectangle', cropped_img)


grid_size = 5

height, width = cropped_img.shape

for x in range(0, width - 1, grid_size):
    cv.line(cropped_img, (x, 0), (x, height), 0, 1, 1)

cv.imshow('Gridded', cropped_img)
cv.waitKey(0)

