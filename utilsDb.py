# Function for resizing image

import cv2

def resize(img,rows,cols):
    return cv2.resize(img, (rows,cols) , interpolation =cv2.INTER_CUBIC)

