
# coding: utf-8

# In[1]:

import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import glob
get_ipython().magic('matplotlib inline')


# In[2]:

labels = []
images = []
prefix='grozi_'


# In[3]:

def check_if_db(name):
    return name.split('.')[-1] == 'db'


# In[4]:

in_vitro_data = glob.glob('grozi/inVitro/*')
in_sito_data = glob.glob('grozi/inSitu/*')
index_data = glob.glob('grozi/index2/*')


# In[5]:

for i,folder in enumerate(in_vitro_data):
    label = folder.split('/')[-1]
    folder_glob = glob.glob(folder+'/web/JPEG/*')
    for im in folder_glob:
        if not check_if_db(im):
            images.append(im)
            labels.append(prefix+label)


# In[6]:

for i,folder in enumerate(in_sito_data):
    label = folder.split('/')[-1]
    folder_glob = glob.glob(folder+'/video/*')
    for im in folder_glob:
        if not check_if_db(im):
            images.append(im)
            labels.append(prefix+label)


# In[7]:

for im in index_data:
    if im.split('.')[-1] != 'txt':
        label = im.split('.')[0].split('/')[-1]
        labels.append(prefix+label)
        images.append(im)


# In[12]:

df = pd.DataFrame({
        'label': labels,
        'file': images
    })


# In[14]:

df.to_csv('grozi.csv')


# In[ ]:



