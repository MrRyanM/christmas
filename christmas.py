import RPi.GPIO as GPIO
import time

flowerBed = 31
eastWindow = 32
bathWindow = 33
post = 35
canes = 36
roof1 = 37
roof2 = 40
inflate = 38
roof = (roof1,roof2)
list = [31,32,33,35,36,37,40]
automated = [31,32,33,35,36,roof]

GPIO.setmode(GPIO.BOARD)

# turn on inflatables
GPIO.setup(inflate, GPIO.OUT)
GPIO.output(inflate, GPIO.HIGH)

# turns each on and off every 2 seconds
def seq():
  for i in automated:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
    time.sleep(2)
    GPIO.output(i, GPIO.HIGH)

# turns each on 1 at a time and keeps
# on until all are on for 5 seconds,
# then all turn off and repeats
def seqHold():
  for i in automated:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
    time.sleep(2)
  time.sleep(3)
  GPIO.output(list, GPIO.HIGH)

try:
  while True:
    for i in range(2):
      seq()
    for i in range(2):
      seqHold()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print (" Quit")
# clean GPIO settings
GPIO.cleanup()
