import cv2
from matplotlib import pyplot as plt
import math

def increase_size(image, size=320):
    shape = image.shape
    top = 0
    bottom = 0
    left  = 0
    right = 0
    if shape[1] < size:
        n = size - shape[1]
        if n%2==1:
            left = n // 2
            right = n // 2 + 1
        else:
            left = n //2
            right = n//2
    if shape[0] < size:
        n = size - shape[0]
        if n%2==1:
            top = n // 2
            bottom = n // 2 + 1
        else:
            top = n //2
            bottom = n //2
    im = cv2.copyMakeBorder(image,top,bottom,left,right,cv2.BORDER_CONSTANT,value=[0,0,0])
    return im


def fix_size(image, size=320):
    shape = image.shape
    if (shape[0] > size) and (shape[1] > size):
        if shape[0] >= shape[1]:
            ratio = math.ceil(shape[0] / size)
        else:
            ratio = math.ceil(shape[1] / size)
        im = cv2.resize(image, (shape[1]//ratio, shape[0]//ratio), interpolation = cv2.INTER_CUBIC)
        return increase_size(im,size)

    elif (shape[0] > size):
        ratio = math.ceil(shape[0] / size)
        im = cv2.resize(image, (shape[1]//ratio, shape[0]//ratio), interpolation = cv2.INTER_CUBIC)
        return increase_size(im,size)

    elif (shape[1] > size):
        ratio = math.ceil(shape[1] / size)
        im = cv2.resize(image, (shape[1]//ratio, shape[0]//ratio), interpolation = cv2.INTER_CUBIC)
        return increase_size(im,size)

    else:
        return increase_size(image, size)
