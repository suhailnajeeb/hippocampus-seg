# Step 1

import nibabel as nib
import numpy as np
import glob
import pandas as pd

# step 2

img_fldr = '' # modify here
files = glob.glob(img_fldr + "*.gz")

datas = [] 

# Step 3

for filePath in files:
    # load image, use the load function
    # get data from image, use the get_fdata function
    # get size of the image. use the shape function
    # append the data to the array named datas. use the append(...) function

# Step 4

df = pd.DataFrame(datas, columns = ['Xsize','Ysize','Zsize'])
df.describe()