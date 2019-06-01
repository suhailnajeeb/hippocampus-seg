import nibabel as nib
import glob

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

singleSlice = data[20,:,:]
singleMask = maskData[20,:,:]

import h5py

h5file = h5py.File("./data/testfile.h5","w")
h5file.create_dataset("image",singleSlice.shape)
h5file.create_dataset("mask",singleMask.shape)

h5file["image"][...] = singleSlice
h5file["mask"][...] = singleMask

h5file.close()

# import matplotlib.pyplot as plt

# plt.figure()
# plt.subplot(1,2,1)
# plt.imshow(singleSlice)
# plt.title("MRI Scan")

# plt.subplot(1,2,2)
# plt.imshow(singleMask)
# plt.title("Label")

# plt.show()

# # Lets recall what I want to do:



