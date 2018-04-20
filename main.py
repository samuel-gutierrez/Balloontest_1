# INFO:
# 1.- Main program for balloon test.
#

# IDEA:
# 1.- Dada cierta condicion, el programa comienza a correr.
#     Esta condicion puede ser una medida de presion, o de altura.
# 2.- Dentro del programa, se toman fotos continuamente, digamos, cada 30 seg.
# 3.- Por cada foto tomada, se guarda y se analiza en funcion del peso o el color.
# 4.- Si la foto cumple la condicion, podria eventualmente enviarse. Esta misma foto pasa al program del ST.
# 5.- Se guarda el resultado de ST: nombre de la foto y los parametros de orientacion.
# 6.- Repeat.

# 1.- Python imports.
import task1

# 2.- Code.
thresh = 10
ard_data = 11

if ard_data > thresh:
    task1.take_pic('pic1')
