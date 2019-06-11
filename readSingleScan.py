# notice me senpai

import nibabel as nib
import glob
import numpy as np

scanID = "hippocampus_001"

scanPath = "./Task04_Hippocampus/imagesTr/"+ scanID + ".nii.gz"
labelPath = "./Task04_Hippocampus/labelsTr/"+scanID + ".nii.gz"

img = nib.load(scanPath)
scan = img.get_fdata()

mask = nib.load(labelPath)
maskData = mask.get_fdata()

#slic = scan[:,20,:]