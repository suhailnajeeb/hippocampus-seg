

import nibabel as nib
import numpy as np

filePath = 'hippocampus_001.nii.gz'
img = nib.load(filePath)
data = img.get_fdata()

slice = data[:,:,20]

import matplotlib.pyplot as plt

plt.imshow(slice)
plt.show()

np.amax(data)
np.amin(data)
