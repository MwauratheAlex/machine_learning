#!/usr/bin/env python3

import cv2 as cv

img = cv.imread("photos/park.jpg")
cv.imshow("Boston", img)

# Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("BnW Boston", gray)

# Blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # kernelSize: (3,3)->less blur, (7,7)->more blur
cv.imshow("Blur", blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175) # Reduce edges by blurring the image
cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dialated", dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)

# Resize
# Ignores aspect ratio
# cv.INTER_CUBIC -> Highest Quality, Slowest
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Cropping
# Images are arrays -> array slicing
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
