# 1.- Imports.
import os
import matplotlib.pyplot as plt
from PIL import Image

# 2.- Functions definition.

DIR_img = './Sample_pics/'


def take_pic(name):
    aux1 = 'raspistill -o ' + str(name)+ '.jpg'
    os.system(aux1)


def return_histo(name):
    file1 = DIR_img + str(name) + '.jpg'
    im = Image.open(file1)
    histo = im.histogram()
    im.show()
    return histo
