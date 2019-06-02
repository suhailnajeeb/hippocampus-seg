import h5py

h5file = h5py.File("./data/testfile.h5","r")

singleSlice = h5file["image"][...]
singleMask = h5file["mask"][...]

h5file.close()

import matplotlib.pyplot as plt

plt.figure()
plt.subplot(1,2,1)
plt.imshow(singleSlice)
plt.title("MRI Scan")

plt.subplot(1,2,2)
plt.imshow(singleMask)
plt.title("Label")

plt.show()