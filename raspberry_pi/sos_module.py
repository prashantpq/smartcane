import RPi.GPIO as GPIO
import time

BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def check_sos():
    if GPIO.input(BUTTON) == GPIO.HIGH:
        print("SOS Button Pressed!")
        return True
    return False
