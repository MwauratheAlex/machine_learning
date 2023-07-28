#!/usr/bin/env python3
import cv2 as cv
import numpy as np

img = cv.imread("photos/park.jpg")
cv.imshow("Boston", img)

# Translation
# Shifting an image along x and y axis. eg. up, down, left, right
# -x    -> Left
# -y    -> Up
# +x    -> Right
# +y    -> Down

def translation(img, x, y):
    translation_matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) #width * height

    return cv.warpAffine(img, translation_matrix, dimensions)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotation_matrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)

# Translate
translated = translation(img, -100, 100)
cv.imshow("Translated", translated)

# Rotate
rotated = rotate(img, -90)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, 90)
cv.imshow("Rotated Rotated", rotated_rotated)

# Resizing
resize = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow("Resized", resize)

# Flipping
# 0 -> Flip image vertically
# 1 -> Flip image horizontally. ie. over the y axis
# -1 -> Flip image both verticall and horizontally
flip = cv.flip(img, 1)
cv.imshow("Flipped", flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
