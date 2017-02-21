
# process dataset Food 11 http://grebvm2.epfl.ch/lin/food/Food-11.zip

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import glob
from collections import Counter

food_11_train_data = glob.glob('food-11/training/*.jpg')
food_11_val_data = glob.glob('food-11/validation/*.jpg')
food_11_test_data = glob.glob('food-11/evaluation/*.jpg')

labels = []
file_names = []

for file in food_11_train_data:
    label = file.split('/')[-1].split('_')[0]
    file = file
    file_names.append(file)
    labels.append(label)

for file in food_11_test_data:
    label = file.split('/')[-1].split('_')[0]
    file = file
    file_names.append(file)
    labels.append(label)

for file in food_11_val_data:
    label = file.split('/')[-1].split('_')[0]
    file = file
    file_names.append(file)
    labels.append(label)

counts = Counter(labels)
df = pd.DataFrame({
        'file': file_names,
        'label': labels
    })
df.to_csv('food_11.csv')
