# process dataset FIDS30 http://data.vicos.si/datasets/FIDS30/FIDS30.zip

import pandas as pd
import numpy as np
import glob
from matplotlib import pyplot

labels = []
image_files = []
folders = glob.glob('FIDS30/*')

for i,f in enumerate(folders):
    fruit = not f.split('.')[-1] == 'txt'
    if fruit:
        label = 'fid'+str(i)
        f_glob = glob.glob(f+'/*')
        for image in f_glob:
            labels.append(label)
            image_files.append(image)

df = pd.DataFrame({'label' : labels, 'file': image_files})
df.to_csv('fids30.csv')
