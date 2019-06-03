import nibabel as nib
import numpy as np
import glob
import pandas as pd
import statistics

img_fldr = './Task04_Hippocampus/imagesTr/'
files = glob.glob(img_fldr + "*.gz")

datas = []

for filePath in files:
    img = nib.load(filePath)
    data = img.get_fdata()
    datas.append([min(data) , max(data), statistics.mean(data)])

df = pd.DataFrame(datas, columns = ['min','max','mean'])
df.describe()