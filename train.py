import h5py
from sklearn.model_selection import train_test_split
import numpy as np

h5path = "./data/train_4x.h5"
h5file = h5py.File(h5path, "r")

n = h5file["image"].shape[0]
a = np.arange(n)

train, test = train_test_split(a, test_size=0.2, random_state=42)

def generator(h5file, indexes, batch_size):
    X = []
    Y = []
    idx = 0
    while True:
        for index in indexes:
            if(idx==0):
                X = []
                Y = []
            print("Loading image : " + str(index) + " , idx = " + str(idx))
            img = np.expand_dims(h5file["image"][index], axis = 2)
            mask = np.expand_dims(h5file["mask"][index], axis = 2)
            X.append(img)
            Y.append(mask)
            idx = idx + 1
            if(idx>=batch_size):
                print("yielding")
                idx = 0
                yield np.asarray(X),np.asarray(Y)

train_generator = generator(h5file, train, 32)
test_generator = generator(h5file, test, 32)

# Define the Model

# Compile the Model & Configure

# Fit the Model

# Plot metrics 

h5file.close()