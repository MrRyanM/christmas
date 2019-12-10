import RPi.GPIO as GPIO
p = [31,32,33,35,36,37,38,40]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(p, GPIO.OUT)
GPIO.cleanup()
