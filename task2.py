import task1
import time

altt_thr = 10
time_init, time_start_prog, time_end_prog = task1.get_time()
print 'INIT TIME          :', time_init
print 'START PROGRAM TIME :', time_start_prog

while True:

    altt_data = 5
    time_now1 = task1.get_time()[0]
    print 'CURRENT TIME       :', time_now1

    if altt_data >= altt_thr or time_now1 >= time_start_prog:
        break

    time.sleep(1)

while True:

    name1 = task1.take_pictures()
    time_now2 = task1.get_time()[0]
    print time_now2
    print time_end_prog

    if time_now2 >= time_end_prog:
        break

    time.sleep(3)

print ' '
