#!/usr/bin/env python3
import cv2 as cv
import matplotlib.pyplot as plt

"""
Color Spaces: spaces of color ^-^
eg. BGR, Black and White. e.t.c
"""

img = cv.imread("photos/park.jpg")
cv.imshow("Park", img)

#plt.imshow(img)
#plt.show()

# BGR -> Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR -> HSV (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("Hsv", hsv)

# BGR -> LAB (L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR -> RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

cv.waitKey(0)
