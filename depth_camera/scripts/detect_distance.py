#!/usr/bin/env python3
"""Detecting distance from image using intel D435i depth camera"""

import cv2
import pyrealsense2 as rs

try:
    # Create a context object. Object owns handle to all connected realsense devices.
    pipeline = rs.pipeline()

    # Configure streams
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

    # Start streaming
    pipeline.start(config)

    while True:
        # This call waits until a new coherent set of frames is available on device
        # Calls to get_frame_data (...) and get_frame_timestamp(...) on a device will reurn stable
        # values until wait_for_frame(...) is called
        frames = pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        if not depth:
            continue

        # Print a simple text based representation of the image, by braking it into 10 x 20
        # pixel regions and approximating the coverage of pixel within one meter
        coverage = [0] * 64
        for y in range(480):
            for x in range(640):
                dist = depth.get_distance(x, y)
                if 0 < dist and dist < 1:
                    coverage[x//10] += 1

            if  y%20 == 19:
                line = ""
                for c in coverage:
                    line += " .:nhBXWW"[c//25]
                coverage = [0]*64
                print(line)

    exit(0)

except Exception as e:
    print(e)
    pass
