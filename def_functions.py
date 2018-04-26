# 1.- Imports.

import datetime
import time
import os
from PIL import Image

# 2.- Functions definition.

DIR_img = './Sample_pics/'


def get_time():
    now = datetime.datetime.now()
    delta1 = datetime.timedelta(seconds=5)
    delta2 = datetime.timedelta(seconds=10)
    delta3 = datetime.timedelta(seconds=15)
    task1_prog = now + delta1
    task2_prog = now + delta2
    task3_prog = now + delta3
    return now, task1_prog, task2_prog, task3_prog


def take_pictures():
    time_list = [10, 20, 40, 60, 80, 100, 200, 300, 400, 500, 600, 700, 800]
    now = get_time()[0]
    name1 = now.strftime('%y%m%d_%H%M%S')
    for i in range(0, len(time_list)):
        name2 = name1 + '_exp' + str(time_list[i])
        aux1 = 'raspistill -w 1024 -h 1024 -t 1 -ss ' + str(time_list[i]) + '000 -o ' + name2 + '.jpg'
        print aux1
        os.system(aux1)
        time.sleep(0.1)
    return name1


def how_black(name):
    file1 = DIR_img + str(name) + '.jpg'
    im = Image.open(file1)
    pixels = im.getdata()
    black_thresh = (80, 80, 80)
    nblack = 0
    n1 = len(pixels)
    for pixel in pixels:
        if pixel < black_thresh:
            nblack += 1
    black = nblack / float(n1)
    return black