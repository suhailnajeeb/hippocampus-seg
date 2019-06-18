import nibabel as nib
import numpy as np
import glob
import pandas as pd

img_fldr = './Task04_Hippocampus/imagesTr/'
files = glob.glob(img_fldr + "*.gz")

datas = []

for filePath in files:
    #filePath = files[0]
    img = nib.load(filePath)
    data = img.get_fdata()
    datas.append(data.shape)

df = pd.DataFrame(datas, columns = ['Xsize','Ysize','Zsize'])
df.describe()