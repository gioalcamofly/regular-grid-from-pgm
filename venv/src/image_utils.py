import cv2 as cv
import numpy as np


GRID_SIZE = 5


def to_higher_multiple(number, multiple):

    while number % multiple != 0:
        number = number + 1

    return number


def get_thresh_img(img, min_thresh, max_thresh):

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    return cv.threshold(gray_img, min_thresh, max_thresh, 0)


def get_bounding_rectangle(thresh_img):

    contours = cv.findContours(thresh_img, 1, 2)
    cnt = contours[0]
    return cv.boundingRect(cnt)


def from_grid_to_image(i, j):

    superior_left_corner = (GRID_SIZE * i, GRID_SIZE * j)

    return superior_left_corner


def find_obstacle(a):

    for i in a:
        for j in i:
            if j <= 240:
                return 1

    return 0


def draw_rectangles_in_image_per_row(img, regular_grid, row_number):

    for i, value in enumerate(regular_grid[row_number]):
        corner = from_grid_to_image(i, row_number)
        if value == 1:
            img = cv.rectangle(img, (corner[0], corner[1]),
                                           (corner[0] + GRID_SIZE, corner[1] + GRID_SIZE), (255, 0, 0), 1)
        else:
            img = cv.rectangle(img, (corner[0], corner[1]),
                                           (corner[0] + GRID_SIZE, corner[1] + GRID_SIZE), (0, 255, 0), 1)

    return img


def draw_rectangle(img, i, j):

    corner = from_grid_to_image(j, i)
    img = cv.rectangle(img, (corner[0], corner[1]), (corner[0] + GRID_SIZE, corner[1] + GRID_SIZE), 127, 1)

    return img



def create_grid(img, height, width):

    regular_grid = np.zeros((height / GRID_SIZE, width / GRID_SIZE), dtype=int)

    for i, row in enumerate(regular_grid):
        for j, value in enumerate(row):
            corner = from_grid_to_image(i, j)
            grid = img[corner[0]:(corner[0] + GRID_SIZE), corner[1]:(corner[1] + GRID_SIZE)]
            regular_grid[i, j] = find_obstacle(grid)

    return regular_grid


def treat_img(img):

    ret, thresh_img = get_thresh_img(img, 240, 255)

    x, y, w, h = get_bounding_rectangle(thresh_img)

    w = to_higher_multiple(w, GRID_SIZE)
    h = to_higher_multiple(h, GRID_SIZE)

    cropped_img = thresh_img[y:(y + h), x:(x + w)]

    regular_grid = create_grid(cropped_img, h, w)

    return cropped_img, regular_grid