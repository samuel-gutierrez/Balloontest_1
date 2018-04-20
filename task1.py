
# 1.- Imports.

import os

# 2.- Functions definition.

def take_pic(name):
    aux1 = 'raspistill -o ' + str(name)+ '.jpg'
    os.system(aux1)

