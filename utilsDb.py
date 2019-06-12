# Function for resizing image

import cv2

def resize(img,rows,cols):
    '''
    pass the image and row/col shape
    returns resized image

    '''
    return cv2.resize(img, (cols,rows) , interpolation =cv2.INTER_CUBIC)

def capScan(scan,thresh):
    f = lambda x : thresh if x>thresh else x
    capped = np.zeros(data.shape)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                capped[i][j][k] = f(data[i][j][k])
    return capped


def normalize(scan,max):
    return scan/4000.0



thresh = 4000
f = lambda x : thresh if x>thresh else x

clipped = map(f,img)

x = list(map(f,singleSlice))

import h5py

h5file = h5py.File("./data/testfile.h5","r")

singleSlice = h5file["image"][...]
singleMask = h5file["mask"][...]

h5file.close()