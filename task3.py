img_fldr = './Task04_Hippocampus/imagesTr/'
label_fldr = './Task04_Hippocampus/labelsTr/'

fileName = 'hippocampus_001.nii.gz'

import os
scanPath = os.path.join(img_fldr,fileName)
labelPath = os.path.join(label_fldr,fileName)

sliceNo = 10

import nibabel as nib

scanImg = nib.load(scanPath)
dataImg = scanImg.get_fdata()
img = dataImg[sliceNo, :, :]

scanLabel = nib.load(labelPath)
dataLabel = scanLabel.get_fdata()
label = dataLabel[sliceNo, :, :]

import matplotlib.pyplot as plt

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("MRI Scan")

plt.subplot(1,2,2)
plt.imshow(label)
plt.title("Label")

plt.show()


