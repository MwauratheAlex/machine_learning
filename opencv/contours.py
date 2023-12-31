#!/usr/bin/env python3
import cv2 as cv
import numpy as np


img = cv.imread("photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", gray)

# 1. Using canny edge detector (Prefer this)

#blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow("Blur", blur)

#canny = cv.Canny(blur, 125, 175) #edges
#cv.imshow("Canny", canny)

# 2.
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

# find contours
contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found")

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours", blank)

cv.imshow("Thresh", thresh)

cv.waitKey(0)
