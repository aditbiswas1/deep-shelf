
# coding: utf-8


import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import glob

labels = []
images = []
prefix='webmarket_'


def check_if_qr(name):
    return name.split('.')[-1] == 'qr'


in_wm_qr_data = glob.glob('qr/qr/*')

for i,folder in enumerate(in_wm_qr_data):
    label = folder.split('/qr')[-1]
    folder_glob = glob.glob(folder)
    for im in folder_glob:
        if not check_if_qr(im):
            images.append(im)
            label = label.split('.jpg')[0]
            labels.append(prefix+label)

df = pd.DataFrame({
    'label': labels,
    'file': images
})

df.to_csv('web_market.csv')

