import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
sw = 27
s = 18
GPIO.setup(sw, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(s, GPIO.OUT)
wervo = GPIO.PWM(s,100)
servo.start(5)
state = False

while True:
    if GPIO.input(sw) == 0
        