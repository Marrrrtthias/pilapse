from time import sleep
from datetime import datetime
import os
import picamera

INTERVAL = 30
startDate = datetime.now()
picDir = '~/pilapse/pilapses/' + startDate.strftime("%Y-%m-%d_%H-%M-%S") + '/'

os.makedirs(picDir)

with picamera.PiCamera() as camera:
	camera.resolution = (1920, 1080)
	for filename in camera.capture_continuous(picDir + 'img-{timestamp:%H-%M-%S-%f}.jpg'):
		sleep(INTERVAL)
