import nibabel as nib
import glob
import numpy as np

scanPath = './Task04_Hippocampus/imagesTr/*.gz'
labelPath = './Task04_Hippocampus/labelsTr/*.gz'

#axis = 'X'

scans = glob.glob(scanPath)
labels = glob.glob(labelPath)

scan = scans[0]
label = labels[0]


img = nib.load(scan)
data = img.get_fdata()

mask = nib.load(label)
maskData = mask.get_fdata()

xsize = 35
ysize = 50
zsize = 35

# take slices along the yz plane:
'''
slices = []

n = data.shape[0]
for i in range(n):
    slices.append(data[i,:,:])
'''

slic = data[0,:,:]
line = slic[0]




#line = list(map(f,line))

def capScan(scan,thresh):
    f = lambda x : thresh if x>thresh else x
    capped = np.zeros(data.shape)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                capped[i][j][k] = f(data[i][j][k])
    return capped

def normalize(scan,max):
    return scan/4000

# todo with a single slice:
'''

import h5py

h5file = h5py.File("./data/testfile.h5","w")
h5file.create_dataset("image",singleSlice.shape)
h5file.create_dataset("mask",singleMask.shape)

h5file["image"][...] = singleSlice
h5file["mask"][...] = singleMask

h5file.close()

'''