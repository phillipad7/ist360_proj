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

    t_diff = abs(pir1_last - pir2_last)
    t1 = start - pir1_last
    t2 = start - pir2_last

    if not t1 or not t2:
        print("t1:{}\nt2:{}\n".format(t1,t2))
    if t_diff < 1:
        print("it's been less than 1 second since both PIRs were activated")
    else:
        print('longger than 1 second')

# change GPIO.RISING to GPIO.FALIING if your PIRs are active low 
GPIO.add_event_detect(12, GPIO.RISING, callback=callback_func)
GPIO.add_event_detect(4, GPIO.RISING, callback=callback_func)

# def main():
#     while True:
#         print( "Not blocking! You're free to do other stuff here")
#         time.sleep(10)


# if __name__=="__main__":
#     GPIO.add_event_detect(12, GPIO.RISING, callback=callback_func)
#     GPIO.add_event_detect(4, GPIO.RISING, callback=callback_func)



# GPIO.add_event_detect(12, GPIO.RISING)  # add rising edge detection on a channel
# GPIO.add_event_detect(4,  GPIO.RISING)  #for both buttons

start = time.time()
while True:
    if GPIO.event_detected(12):
        print('PIR 1 detect')
    if GPIO.event_detected(4):
        print('PIR 2 detect')
    # if time.time() - start > 5:
    #     print('Timeout')
    time.sleep(0.1)