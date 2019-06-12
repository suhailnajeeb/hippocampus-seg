# Function for resizing image

import cv2
import numpy as np

def resize(img,rows,cols):
    '''
    pass the image and row/col shape
    returns resized image

    '''
    return cv2.resize(img, (cols,rows) , interpolation = cv2.INTER_CUBIC)

def resizeStack(stack,plane,size):
    '''
    resize a stack of images
    '''
    xsize, ysize, zsize = size
    if plane == 'yz':
        resized = [resize(slic,ysize,zsize) for slic in stack]
    if plane == 'zx':
        resized = [resize(slic,zsize,xsize) for slic in stack]
    if plane == 'xy':
        resized = [resize(slic,xsize,ysize) for slic in stack]
    return resized


def capScan(scan,thresh):
    f = lambda x : thresh if x>thresh else x
    capped = np.zeros(scan.shape)
    for i in range(scan.shape[0]):
        for j in range(scan.shape[1]):
            for k in range(scan.shape[2]):
                capped[i][j][k] = f(scan[i][j][k])
    return capped


def normalize(scan,max):
    return scan/4000.0

def return2DslicesAsList(scan,plane):
    '''
    Takes in a 3D Scan and returns slices as a list along
    axis defined by plane. 
    plane = 'yz' , 'zx', 'xy'
    '''
    slices = []
    if plane == 'yz':
        for i in range(35):
            slices.append(scan[i,:,:])
    if plane == 'zx':
        for i in range(scan.shape[1]):
            slices.append(scan[:,i,:])
    if plane == 'xy':
        for i in range(scan.shape[2]):
            slices.append(scan[:,:,i])
    return slices






'''

thresh = 4000
f = lambda x : thresh if x>thresh else x

clipped = map(f,img)

x = list(map(f,singleSlice))

import h5py

h5file = h5py.File("./data/testfile.h5","r")

singleSlice = h5file["image"][...]
singleMask = h5file["mask"][...]

h5file.close()
'''