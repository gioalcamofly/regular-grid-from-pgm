import cv2 as cv
import sys
from astar import astar
from dfs import dfs
from bfs import bfs
from image_utils import treat_img, draw_rectangle
import copy
import time

img = cv.imread('./resources/housemap.pgm')

if img is None:
    sys.exit('Can\'t read image')


treated_img, regular_grid = treat_img(img)

start = (1, 1)
print regular_grid[10, 50]
end = (11, 8)

start_time = time.time()
path = astar(regular_grid, start, end)
astar_time = time.time() - start_time

start_time = time.time()
dfs_path = dfs(regular_grid, start, end)
dfs_time = time.time() - start_time

start_time = time.time()
bfs_path = bfs(regular_grid, start, end)
bfs_time = time.time() - start_time

astar_image = copy.copy(treated_img)
dfs_image = copy.copy(treated_img)
bfs_image = copy.copy(treated_img)

for node in path:
    astar_image = draw_rectangle(astar_image, node[0], node[1])

for node in dfs_path:
    dfs_image = draw_rectangle(dfs_image, node[0], node[1])

for node in bfs_path:
    bfs_image = draw_rectangle(bfs_image, node[0], node[1])

cv.imshow('astar_path', astar_image)
cv.imshow('dfs_path', dfs_image)
cv.imshow('bfs_path', bfs_image)

cv.waitKey(0)

print(len(path))
print(len(dfs_path))
print(len(bfs_path))

print astar_time
print dfs_time
print bfs_time
