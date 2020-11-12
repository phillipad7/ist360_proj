import time
# import board
# import digitalio
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)


root_path = '/home/pi/test_py'
mp3 = os.path.join(root_path, 'brake5s.mp3')
print(mp3)


# wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
channel1 = GPIO.wait_for_edge(12, GPIO_RISING, timeout=5000)
channel1 = GPIO.wait_for_edge(4, GPIO_RISING, timeout=5000)


if channel is None:
    print('Timeout occurred')
else:
    print('Edge detected on channel', channel)


GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel
do_something()
if GPIO.event_detected(channel):
    print('Button pressed')



def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)  # add rising edge detection on a channel






while True:
    time.sleep(10)
    print('1')
    # if pirSensor1.value and pirSensor2.value:
    #     print("PIR ALARM!")
    #     print(pirSensor1.value, pirSensor2.value)
    #     os.system('omxplayer ' + mp3 + ' &')
    #     send_email.sendEmail()

    # elif pirSensor1.value and not pirSensor2.value:
    #     print('human passing through')
    #     print(pirSensor1.value, pirSensor2.value)
    #     send_email.sendEmail(subject='Sent from rpi zero')
    # time.sleep(3)
