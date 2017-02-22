import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

def visualize_class(class_id, sample_size=3):
    gs = gridspec.GridSpec(1, sample_size, top=1., bottom=0., right=0.8, left=0., hspace=0.,
        wspace=0.5)

    images_for_class = data[data['label'] == class_id]['file']
    random_image_files = images_for_class.sample(n=sample_size)
    figure = plt.figure(figsize=(3,10))
    images = [plt.imread(im) for im in random_image_files]
    for i,im in enumerate(images):
        ax = plt.subplot(gs[i])
        plt.imshow(im)
        ax.axis("off")
    plt.title(class_id)

data = pd.read_csv('grozi.csv')
classes = data['label'].unique()


for class_id in classes:
    visualize_class(class_id)

