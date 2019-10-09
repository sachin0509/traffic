the traffic light will run in the background  with a time interval of 'X'
>>camera on
>>start recording{
	while signal==red
		{
		if motion is sensed
			{
			capture image> timestamp> save in cloud
			}
		}
		}
		else continue recording/flow of lights



from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
from subprocess import call

#create objects that refer to a,
#a motion sensor and the PiCamera
pir = MotionSensor(4)
camera = PiCamera()
#image name
i=0

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def take_photo():
    	global i
   	i = i + 1
	filePath = "/home/pi/Desktop/projectpic/image_%s.jpg' %i"
	currentTime=datetime.now()
	camera.capture(filePath)
	print('picture saved')
    
    timestampMessage = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    
	# Create time stamp command to have executed
    timestampCommand = "/usr/bin/convert " + filePath + " -pointsize 36 \
    -fill red -annotate +700+650 '" + timestampMessage + "' " + filePath
    	# Actually execute the command!
    call([timestampCommand], shell=True)
	print('pic timestamped')


while True: 
      # Red 
    camera.rotation = 180
    camera.start_preview()
    GPIO.output(9, True) 
    time.sleep(3)
    pir.when_motion=take_photo()
    print('Red light Jumper captured!')
    camera.stop_preview()

      # Red and amber 
    GPIO.output(10, True) 
    time.sleep(1)  

	# Green 
    GPIO.output(9, False) 
    GPIO.output(10, False) 
    GPIO.output(11, True) 
    time.sleep(5)  
    
	# Amber 
   # GPIO.output(11, False) 
    #GPIO.output(10, True) 
   # time.sleep(2)  
    
	# Amber off (red comes on at top of loop) 
    #GPIO.output(10, False)


    
    





