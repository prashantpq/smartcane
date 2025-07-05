import cv2
import time
import threading
import RPi.GPIO as GPIO

from camera_module import detect_objects
from ultrasonic_module import measure_distance, activate_buzzer
from sos_module import check_sos
from bluetooth_module import send_data


cap = cv2.VideoCapture(0)

def distance_buzzer_thread():
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.1f} cm")
        activate_buzzer(dist)
        time.sleep(0.5)

def sos_thread():
    while True:
        if check_sos():
            send_data("SOS")
            time.sleep(1)


t1 = threading.Thread(target=distance_buzzer_thread)
t2 = threading.Thread(target=sos_thread)
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()


try:
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        objects = detect_objects(frame)

        for obj in objects:
            send_data(obj)

        time.sleep(1)

except KeyboardInterrupt:
    cap.release()
    GPIO.cleanup()
    print("Exiting gracefully.")


# run the line in pi4 terminal so that the script can run as soon as pi starts
# crontab -e
# @reboot python3 /home/pi/smart-cane/raspberry_pi/scripts.py &
