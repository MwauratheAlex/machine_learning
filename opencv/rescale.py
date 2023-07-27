#!/usr/bin/env python3
import cv2 as cv

def rescale_frame(frame, scale=0.75):
    # works for videos, images, live camera feed
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def change_res(width, height):
    # Only works for live video, i.e. Camera
    capture.set(3, width)
    capture.set(4, height)


def main():
    capture = cv.VideoCapture("videos/dog.mp4")

    while True:
        isTrue, frame = capture.read()

        if not isTrue:
            break

        frame_resized = rescale_frame(frame, 0.2)
        
        cv.imshow("Video", frame)
        cv.imshow("Video Resized", frame_resized)

        if cv.waitKey(20) & 0xFF == ord("d"):
            break

    
    capture.release()
    cv.destroyAllWindows()

main()

