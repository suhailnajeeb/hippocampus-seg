# Function for resizing image

import cv2

def resize(img,xsize,ysize):
    return cv2.resize(img, (xsize,ysize) , interpolation =cv2.INTER_CUBIC)

