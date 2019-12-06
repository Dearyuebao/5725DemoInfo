                                                      import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT)

p = GPIO.PWM(26, 1)
p.start(50)
print(type(p))
try:
	while True:
		for f in range(1, 11):
			p.ChangeFrequency(f)
			time.sleep(0.1)
		for f in range(11, 0, -1):
			p.ChangeFrequency(f)
			time.sleep(0.1)
except KeyboardInterrupt:
	pass

p.stop()
GPIO.cleanup()


