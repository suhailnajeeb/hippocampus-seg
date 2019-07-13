import nibabel as nib
import glob

# import numpy as np
import h5py
from utilsDb import distort_img

# Utility Imports

from utilsDb import capScan
from utilsDb import normalize
from utilsDb import return2DslicesAsList
from utilsDb import resizeStack

from keras.utils import to_categorical

### global parameters ###

size = [35, 50, 35]                 # dimensions to resize scan to
xsize, ysize, zsize = size
thresh = 4000                       # MRI cutoff value
plane = "xy"                        # set the plane along which scans will be taken
mult = 4                            # factor of augmentation, set 0 for no augmentation

# for train set set Train = true, else set Train = false

Train = True

if Train:
    scanPath = "./Task04_Hippocampus/imagesTr/*.nii.gz" # + scanName
    labelPath = "./Task04_Hippocampus/labelsTr/*.nii.gz" #  + scanName
    h5path = "./data/train_" + str(mult) + ".h5"

else:
    scanPath = "./Task04_Hippocampus/imagesTs/*.nii.gz" # + scanName
    labelPath = "./Task04_Hippocampus/labelsTs/*.nii.gz" #  + scanName  
    h5path = "./data/test.h5"
    mult = 0


# collect image paths from folders

scans = sorted(glob.glob(scanPath))
labels = sorted(glob.glob(labelPath))

# count number of images

nimages = 0

for scan in scans:
    img = nib.load(scan)
    imgData = img.get_fdata()
    if plane == "yz":
        n = imgData.shape[0]
    if plane == "zx":
        n = imgData.shape[1]
    if plane == "xy":
        n = imgData.shape[2]
    nimages = nimages + n

nimages = nimages * (mult + 1)


if plane == "yz":
    shape = (ysize, zsize)
if plane == "zx":
    shape = (zsize, xsize)
if plane == "xy":
    shape = (xsize, ysize)

shape = (nimages,) + shape

h5file = h5py.File(h5path, "w")
h5file.create_dataset("image", shape)
h5file.create_dataset("mask", shape)

def storeSingleImage(didx,scanPath,labelPath):
    img = nib.load(scanPath)
    imgData = img.get_fdata()

    mask = nib.load(labelPath)
    maskData = mask.get_fdata()

    capped = capScan(imgData, thresh)
    slices = return2DslicesAsList(capped, plane)
    scanResized = resizeStack(slices, plane, size)

    masks = return2DslicesAsList(maskData, plane)
    maskResized = resizeStack(masks, plane, size)

    for (scan, mask) in zip(scanResized, maskResized):
        maskCat = to_categorical(mask)
        mask1 = maskCat[:, :, 0]
        mask = 1 - mask1
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
    return didx

didx = 0

for (scanPath,labelPath) in zip(scans,labels):
    print("Processing: " + scanPath)
    didx = storeSingleImage(didx, scanPath, labelPath)

h5file.close()