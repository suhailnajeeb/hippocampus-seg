import h5py

h5file = h5py.File("./data/testfile.h5","r")

singleSlice = h5file["test"][...]

h5file.close()

import matplotlib.pyplot as plt

plt.imshow(singleSlice)
plt.show()

# so this thing is working for a single image.
# Next we will move on to multiple images.
