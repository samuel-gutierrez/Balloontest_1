# INFO:
# 1.- Main program for balloon test.
#

# IDEA:
# 1.- El programa comienza a correr si ocurre una de las siguientes condiciones:
#     a.- El globo alcanza la altura de 15 km.
#     b.- El globo lleva dos horas desde su despegue.
# 2.- Dentro del programa, se toman fotos continuamente.
# 3.- Las fotos se toman con distintos tiempos de exposicion (en ms):
#     20, 40, 60, 80, 100, 200, 300, 400, 500, 600, 700, 800. Todas las fotos se guardan.
# 4.- Por cada foto adquirida, se corre el algoritmo de determinacion de color.
# 5.- Todas las fotos que sean lo suficientemente negras (buscar umbral), se pasan al programa del ST.
# 6.- Si el programa del ST encuentra matching, esa foto se guarda para enviar.
# 7.- Cuando el programa del ST culmina, se vuelven a tomar fotos.
# 8.- Si dado cierto tiempo (15 min) no se ha hecho ningun matching, el programa guarda una foto de las negras ...
#     para enviar (por definir).
# 9.- Sigue ejecutando esta accion por 2 horas, o hasta que se detecte que se corto un globo.
# 10.- Finalmente, se corre el algoritmo de RJ por dos horas mas.
# 11.- RPI off

# 1.- Python imports.
import task1

# # 2.- Code.
#
# altt_thr = 10
# altt_data = 11
# time1 = 15
#
#
# # if altitude_data >= altitude_thr:
# #    task1.take_pic('pic1')

img_name = 'pic1'
a, R, G, B = task1.return_histo(img_name)

# now = task1.get_current_time()
#
# print a
# print now
#
#
# h1 = 18
# h1ref = 15
# time1 = 17
# time1ref = 15
#
# if h1 >= h1ref or time1 >= time1ref:
#     print ' --- asdf ---'
# else:
#     pass
#
#
