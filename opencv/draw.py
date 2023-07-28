#!/usr/bin/env python3
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500,3), dtype="uint8") #height, width, no. of Color Channels
#img = cv.imread("photos/cat.jpg")

#cv.imshow("Cat", img)
#cv.imshow("Blank", blank)

# 1. Paint image a given color
blank[200:300, 300:400] = 0,255,255

# 2. Draw a rectangle
#cv.rectangle(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (0, 255,0), thickness=2)

# 3. Draw a circle
#cv.circle(blank, (250,250), 80, (0, 0, 255), thickness=2)

# 4. Draw a line
cv.line(blank, (0,0), (500,500), (0,255,255), thickness=4)

# 5. Text on an image
cv.putText(blank, "Mwaura", (0,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)

cv.imshow("Green", blank)

cv.waitKey(0)
