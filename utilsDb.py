# Function for resizing image

import cv2

def resize(img,rows,cols):
    '''
    pass the image and row/col shape
    returns resized image

    '''
    return cv2.resize(img, (cols,rows) , interpolation =cv2.INTER_CUBIC)

