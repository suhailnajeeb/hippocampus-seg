import nibabel as nib
import glob
import numpy as np
import h5py

# Utility Imports

from utilsDb import capScan
from utilsDb import normalize
from utilsDb import return2DslicesAsList
from utilsDb import resizeStack

### global parameters ###

size = [35,50,35]
thresh = 4000
plane = 'xy'

scanName = 'hippocampus_001.nii.gz'

scanPath = './Task04_Hippocampus/imagesTr/' + scanName
labelPath = './Task04_Hippocampus/labelsTr/' + scanName

#scans = glob.glob(scanPath)
#labels = glob.glob(labelPath)

#scan = scans[0]
#label = labels[0]

###################### for a single image ##################################

img = nib.load(scanPath)
imgData = img.get_fdata()

mask = nib.load(labelPath)
maskData = mask.get_fdata()

capped = capScan(imgData,thresh)
slices = return2DslicesAsList(capped,plane)
scanResized = resizeStack(slices,plane,size)

masks = return2DslicesAsList(maskData, plane)
maskResized = resizeStack(masks,plane,size)

# todo: store all the images of a scan inlcuding mask in an h5 file.

# todo: apply compression and formatting to dataset

nimages = len(scanResized)
shape = (nimages,) + scanResized[0].shape

h5file = h5py.File("./data/testfile.h5","w")
h5file.create_dataset("image",shape)
h5file.create_dataset("mask",(nimages,) + shape)

didx = 0

for img in scanResized:
    h5file["image"][didx] = normalize(img,thresh)
    didx = didx + 1

didx = 0
for masks in maskResized:
    h5file["mask"][didx] = masks
    didx = didx + 1

h5file.close()

######################### ends here ############################

# todo: Study the standard deviation and distribution of the dataset

# todo: Resize Scan in all dimensions
