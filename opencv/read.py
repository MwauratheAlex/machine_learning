#!/usr/bin/env python3

import cv2 as cv

def read_image():
    img = cv.imread("photos/cat_large.jpg") #matrix of pixels
    cv.imshow("Cat", img)

def read_video(name="dog.mp4"):
    capture = cv.VideoCapture("videos/{}".format(name)) #takes path or 0->webcam, 1->first cam, ...

    # Read video frame by frame
    while True:
        isTrue, frame = capture.read() # Bool indicates success or not
        if isTrue:
            cv.imshow("Video", frame)

        if not isTrue or (cv.waitKey(20) & 0xFF==ord("d")):
            break

    capture.release()
    cv.destroyAllWindows()

def main():
    #read_image()
    #cv.waitKey(0)
    read_video()

main()
