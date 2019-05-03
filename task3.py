img_fldr = './Task04_Hippocampus/imagesTr/'
label_fldr = './Task04_Hippocampus/labelsTr/'

fileName = 'hippocampus_001.nii.gz'

import os
scanPath = os.path.join(img_fldr,fileName)
labelPath = os.path.join(img_fldr,fileName)

#sliceNo = 10

import nibabel as nib

scan = nib.load(scanPath)
data = scan.get_fdata()

