import RPi.GPIO as GPIO
import time
p = [31,32,33,35,36,37,38,40]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(p, GPIO.OUT)
GPIO.cleanup()
time.sleep(5)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)
