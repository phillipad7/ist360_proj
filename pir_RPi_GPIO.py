import time
# import board
# import digitalio
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)

start = pir1_last = pir2_last = time.time()

def callback_func(pin):
    global pir1_last
    global pir2_last
    t_now = time.time()

    if GPIO.input(12):
        pir1_last = t_now
    if GPIO.input(4):
        pir2_last = t_now

    # t_diff = abs(pir1_last - pir2_last)

    # if t_diff < 1:
    #     print("it's been less than 1 second since both PIRs were activated")
    # else:
    #     print('longger than 1 second')

    t1 = start - pir1_last
    t2 = start - pir2_last

    # if not t1 or not t2:
    print("t1:{}\nt2:{}\n".format(t1,t2))
    

# change GPIO.RISING to GPIO.FALIING if your PIRs are active low 
GPIO.add_event_detect(12, GPIO.RISING, callback=callback_func)
GPIO.add_event_detect(4, GPIO.RISING, callback=callback_func)


start = time.time()

while True:

    d1 = GPIO.event_detected(12)
    d2 = GPIO.event_detected(4)
    # if d1:
    #     print('pin_12 -- d1 true')
    # if d2:
    #     print('pin_4  -- d2 true')


    if d1 and d2:
        print("both sensor detected -- human passing through")
    elif d1 and (not d2):
        print("pin_12 true  pin_4 false -- cat passing")
    elif d2 and (not d1):
        print('pin_12 false pin_4 true  -- ????')
    # else:
    #     print('pin_12:{}\npin_4:{}\n -- neither true -- no motion'.format(d1, d2))


    time.sleep(2)

