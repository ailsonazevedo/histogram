import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def generate_histogram_img(path, text):
    
    img = cv.imread(path)
    
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow(text, img)
    plt.hist(img.ravel(),256,[0,256])
    plt.show()
    cv.waitKey(0)

def convert_to_gray(img):
    return cv.cvtColor(img, cv.COLOR_RGB2GRAY)

def convert_to_rgb(img):
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)

def resize(img, width, height):
    return cv.resize(img, (width, height))