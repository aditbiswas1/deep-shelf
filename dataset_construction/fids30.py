
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import glob
from matplotlib import pyplot


# In[2]:

labels = []
image_files = []


# In[9]:

folders = glob.glob('FIDS30/*')


# In[15]:

for i,f in enumerate(folders):
    fruit = not f.split('.')[-1] == 'txt'
    if fruit:
        label = 'fid_' + str(i)
        f_glob = glob.glob(f+'/*')
        for image in f_glob:
            labels.append(label)
            image_files.append(image)
        


# In[19]:

df = pd.DataFrame({'label': labels, 'file': image_files})


# In[21]:

df.to_csv('fids30.csv')


# In[ ]:



