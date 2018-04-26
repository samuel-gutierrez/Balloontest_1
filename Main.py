# INFO:
# 1.- Main program for balloon test.
#

# IDEA:
# 1.- El programa comienza a correr si ocurre una de las siguientes condiciones:
#     a.- El globo alcanza la altura de 10 km.
#     b.- El globo lleva dos horas desde su despegue.
# 2.- Dentro del programa, se toman fotos continuamente.
# 3.- Las fotos se toman con distintos tiempos de exposicion (en ms):
#     20, 40, 60, 80, 100, 200, 300, 400, 500, 600, 700, 800. Todas las fotos se guardan.
# 4.- Por cada foto adquirida, se corre el algoritmo de determinacion de color.
# 5.- Todas las fotos que sean lo suficientemente negras (buscar umbral), se pasan al programa del ST.
# 6.- Si el programa del ST encuentra matching, esa foto se guarda para enviar.
# 7.- Cuando el programa del ST culmina, se espera un tiempo y se vuelven a tomar fotos.
# 8.- Si dado cierto tiempo (15 min) no se ha hecho ningun matching, el programa guarda una foto de las negras ...
#     para enviar (por definir).
# 9.- Sigue ejecutando esta accion por 2 horas, o hasta que se detecte que se corto un globo.
# 10.- Finalmente, se corre el algoritmo de RJ por dos horas mas.
# 11.- RPI off

# 1.- Imports.
import def_functions
import time

# 2.- Code.
altt_thr = 10
time_init, time_task1, time_task2, time_task3 = def_functions.get_time()
print ' --- START ---'
print 'INIT TIME            :', time_init
print 'REACH ALTTITUDE TIME :', time_task1
print 'DESTROY BALLOON TIME :', time_task2
print 'END EXPERIMENT TIME  :', time_task3

# 2.1.- Task1: Waiting for correct altitude.
print ' --- TASK1 ---'
while True:

    altt_data = 5
    time_now1 = def_functions.get_time()[0]
    print 'CURRENT TIME         :', time_now1

    if altt_data >= altt_thr or time_now1 >= time_task1:
        break

    time.sleep(1)

# 2.2.- Task2: Taking pictures in semi-still state.
print ' --- TASK2 ---'
while True:

    time_now2 = def_functions.get_time()[0]
    print 'CURRENT TIME         :', time_now2
    print 'DESTROY BALLOON TIME :', time_task2
    if time_now2 >= time_task2:
        break

    name1 = def_functions.take_pictures()
    time.sleep(3)

# 2.3.- Task3: Taking pictures of Earth while descending.
print ' --- TASK3 ---'
while True:
    time_now3 = def_functions.get_time()[0]
    print 'CURRENT TIME         :', time_now3
    print 'END EXPERIMENT TIME  :', time_task3
    # Codigo de RJ.
    if time_now3 >= time_task3:
        break
    time.sleep(1)

print ' --- END ---'
