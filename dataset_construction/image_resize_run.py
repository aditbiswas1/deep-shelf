
# coding: utf-8

# In[14]:

from image_resize import fix_size
import csv
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
get_ipython().magic('matplotlib inline')


# In[26]:

with open('fids30.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in spamreader:
        count+=1
        if count == 1:
            continue
        image = mpimg.imread(row[1])
        new_image = image/128. - 1.
        a =plt.imsave(row[1], new_image)
