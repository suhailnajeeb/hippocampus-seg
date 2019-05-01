

import nibabel as nib
import numpy as np

filePath = 'hippocampus_001.nii.gz'
img = nib.load(filePath)
data = img.get_fdata()

print("Shape of the Image:")
print(data.shape)

slice1 = data[0,:,:]
slice2 = data[:,0,:]
slice3 = data[:,:,0]

import matplotlib.pyplot as plt

plt.imshow(slice1)
plt.show()

plt.imshow(slice2)
plt.show()

plt.imshow(slice2)
plt.show()

np.amax(data)
np.amin(data)
