import nibabel as nib
# import glob
# import numpy as np
import h5py
from utilsDb import distort_img

# Utility Imports

from utilsDb import capScan
from utilsDb import normalize
from utilsDb import return2DslicesAsList
from utilsDb import resizeStack

# ## global parameters ###

size = [35, 50, 35]
thresh = 4000
plane = 'xy'

scanName = 'hippocampus_001.nii.gz'

scanPath = './Task04_Hippocampus/imagesTr/' + scanName
labelPath = './Task04_Hippocampus/labelsTr/' + scanName

# scans = glob.glob(scanPath)
# labels = glob.glob(labelPath)

# scan = scans[0]
# label = labels[0]

# ##################### for a single image ##################################

img = nib.load(scanPath)
imgData = img.get_fdata()

mask = nib.load(labelPath)
maskData = mask.get_fdata()

capped = capScan(imgData, thresh)
slices = return2DslicesAsList(capped, plane)
scanResized = resizeStack(slices, plane, size)

masks = return2DslicesAsList(maskData, plane)
maskResized = resizeStack(masks, plane, size)

# todo: store all the images of a scan inlcuding mask in an h5 file.

# todo: store the masks in categorical format

# todo: apply compression and formatting to dataset

mult = 9

nimages = len(scanResized)*(mult+1)
shape = (nimages,) + scanResized[0].shape

h5file = h5py.File("./data/testfile.h5", "w")
h5file.create_dataset("image", shape)
h5file.create_dataset("mask", (nimages,) + shape)

didx = 0

for (scan, mask) in zip(scanResized, maskResized):
    data = [scan, mask]
    scans = [scan]
    masks = [mask]
    for i in range(mult):
        scan_distorted, mask_distorted = distort_img(data)
        scans.append(scan_distorted)
        masks.append(mask_distorted)
    for (img, mask) in zip(scans, masks):
        h5file["image"][didx] = normalize(img, thresh)
        h5file["mask"][didx] = mask
        didx = didx + 1

h5file.close()

"""
didx = 0

for img in scanResized:
    h5file["image"][didx] = normalize(img, thresh)
    didx = didx + 1

didx = 0
for masks in maskResized:
    h5file["mask"][didx] = masks
    didx = didx + 1

h5file.close()

# ######################## ends here ############################

# todo: Study the standard deviation and distribution of the dataset

# todo: Resize Scan in all dimensions

"""