import time
import os
import RPi.GPIO as GPIO
# import schedule
import detection_db
from send_email import sendEmail

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


    t1 = start - pir1_last
    t2 = start - pir2_last

    print("t1:{}\nt2:{}\n".format(t1,t2))
    

# change GPIO.RISING to GPIO.FALIING if your PIRs are active low 
GPIO.add_event_detect(12, GPIO.RISING, callback=callback_func)
GPIO.add_event_detect(4, GPIO.RISING, callback=callback_func)

# testing if email canbe sent along with a loop
sendEmail()


start = time.time()

while True:
    d1 = GPIO.event_detected(12)
    d2 = GPIO.event_detected(4)

    if d1 and d2:
        # print("p_12 T p_4 T -- human")
        detection_db.insert(0)
    elif d1 and (not d2):
        # print("p_12 T p_4 F -- cat")
        detection_db.insert(1)
    elif d2 and (not d1):
        # print('p_12 F p_4 T -- ???')
        detection_db.insert(2)
    # else:
    #     print('pin_12:{}\npin_4:{}\n -- neither true -- no motion'.format(d1, d2))

    time.sleep(2)

    # schedule.every(1).minutes.at(":19").do(sendEmail)

