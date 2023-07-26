#!/usr/bin/env python3
""" Viewing images from depth camera"""

import pyrealsense2 as rs
import numpy as np
import cv2

# Configure depth and color stream
pipeline = rs.pipeline()
config = rs.config()

# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_name = str(device.get_info(rs.camera_info.product_line))

print("Device Name:", device_product_name)



