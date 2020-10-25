import time
import board
import digitalio
import os
import send_email

# set up motion sensor
pirSensor1 = digitalio.DigitalInOut(board.D4)
pirSensor2 = digitalio.DigitalInOut(board.D12)
pirSensor1.direction = digitalio.Direction.INPUT
pirSensor2.direction = digitalio.Direction.INPUT



# set up door sensor
#door_sensor = digitalio.DigitalInOut(board.D23)
#door_sensor.direction = digitalio.Direction.INPUT




root_path = '/home/pi/test_py'
mp3 = os.path.join(root_path, 'brake5s.mp3')
print(mp3)

while True:

    if pirSensor1.value and pirSensor2.value:
        print("PIR ALARM!")
        print(pirSensor1.value, pirSensor2.value)
        os.system('omxplayer ' + mp3 + ' &')
        send_email.sendEmail()

    elif pirSensor1.value and not pirSensor2.value:
        print('human passing through')
        print(pirSensor1.value, pirSensor2.value)
        send_email.sendEmail(subject='Sent from rpi zero')
    time.sleep(3)
