import nibabel as nib
import os
import numpy as np

train_fldr = './Task04_Hippocampus/imagesTr'

scans = os.listdir(train_fldr)

for scan in scans:
    filePath = os.path.join(train_fldr,scan)
    img = nib.load(filePath)
    data = img.get_fdata()
    print("Information for image: " + scan)
    print("Shape of data: " + str(data.shape))
    print("Maximum voxel value:" + str(np.amax(data)))
    print("Minimum voxel value:" + str(np.amin(data)))


