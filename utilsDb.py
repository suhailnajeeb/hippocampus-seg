# Function for resizing image

import cv2

def resize(img,rows,cols):
    '''
    pass the image and row/col shape
    returns resized image

    '''
    return cv2.resize(img, (cols,rows) , interpolation =cv2.INTER_CUBIC)



thresh = 4000
f = lambda x : thresh if x>thresh else x

clipped = map(f,img)

x = list(map(f,singleSlice))

import h5py

h5file = h5py.File("./data/testfile.h5","r")

singleSlice = h5file["image"][...]
singleMask = h5file["mask"][...]

h5file.close()