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

size = [35,50,35]

xsize, ysize, zsize = size
'''
xsize = 35
ysize = 50
zsize = 35
'''
# take slices along the yz plane:
'''
slices = []

n = data.shape[0]
for i in range(n):
    slices.append(data[i,:,:])
'''


thresh = 4000

from utilsDb import capScan
from utilsDb import normalize
from utilsDb import return2DslicesAsList
from utilsDb import resizeStack


capped = capScan(data,thresh)
#normalized = normalize(capped,thresh)
 
zx = return2DslicesAsList(capped,'zx')

resized = resizeStack(zx,'zx',size)



import numpy as np

zx = np.asarray(resized)
print(zx.shape)
 
# todo: Study the standard deviation and distribution of the dataset

# todo: Resize Scan in all dimensions

'''

import h5py

h5file = h5py.File("./data/testfile.h5","w")
h5file.create_dataset("image",singleSlice.shape)
h5file.create_dataset("mask",singleMask.shape)

h5file["image"][...] = singleSlice
h5file["mask"][...] = singleMask

h5file.close()

'''