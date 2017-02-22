
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import glob
from matplotlib import pyplot
import os

# In[2]:

labels = []
image_files = []

labels_to_be_used = ['sweet_pepper', 'apple', 'mushroom', 'orange', 'pear']
# In[9]:
# cifar100_train_data_path = 'cifar100/coarse/train.txt'


for i, each in enumerate(labels_to_be_used):
    cifar100_test_data_path = 'cifar100/coarse/test/fruit_and_vegetables/'
    cifar100_test_data_path = cifar100_test_data_path + each + '/'
    path = os.getcwd() + '/' + cifar100_test_data_path
    for filename in os.listdir(path):
        image_files.append(cifar100_test_data_path + filename)
        labels.append('cifar100_' + str(i))


for i, each in enumerate(labels_to_be_used):
    cifar100_train_data_path = 'cifar100/coarse/train/fruit_and_vegetables/'
    cifar100_train_data_path = cifar100_test_data_path + each + '/'
    path = os.getcwd() + '/' + cifar100_test_data_path
    for filename in os.listdir(path):
        image_files.append(cifar100_test_data_path + filename)
        labels.append('cifar100_' + str(i))
# # In[19]:

df = pd.DataFrame({'label': labels, 'file': image_files})


# # # In[21]:

df.to_csv('cifar100.csv')


# # In[ ]:



