# 1.- Imports.
import datetime
import os
# import matplotlib.pyplot as plt
from PIL import Image
import time

# 2.- Functions definition.

DIR_img = './Sample_pics/'


def take_pic(name):
    aux1 = 'raspistill -o ' + str(name) + '.jpg'
    os.system(aux1)


def return_histo(name):
    file1 = DIR_img + str(name) + '.jpg'
    im = Image.open(file1)
    histo = im.histogram()
    im.show()
    return histo


def get_time():
    now = datetime.datetime.now()
    delta1 = datetime.timedelta(seconds=5)
    delta2 = datetime.timedelta(seconds=10)
    start_prog = now + delta1
    end_prog = now + delta2
    return now, start_prog, end_prog


def take_pictures():
    time_list = [10, 20, 40, 60, 80, 100, 200, 300, 400, 500, 600, 700, 800]
    now = get_time()[0]
    name1 = now.strftime('%y%m%d_%H%M%S')
    for i in range(0, len(time_list)):
        name2 = name1 + '_exp_' + str(time_list[i])
        aux1 = 'raspistill -w 1024 -h 1024 -t 1 -ss ' + str(time_list[i]) + '000 -o ' + name2 + '.jpg'
        print aux1
        os.system(aux1)
        time.sleep(0.1)
    return name1
