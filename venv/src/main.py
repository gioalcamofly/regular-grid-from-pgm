import cv2 as cv
import sys
from astar import astar
from image_utils import treat_img, draw_rectangle

img = cv.imread('./resources/housemap.pgm')

if img is None:
    sys.exit('Can\'t read image')


treated_img, regular_grid = treat_img(img)

start = (1, 1)
end = (10, 10)

path = astar(regular_grid, start, end)

for node in path:
    treated_img = draw_rectangle(treated_img, node[0], node[1])

cv.imshow('path', treated_img)

cv.waitKey(0)

