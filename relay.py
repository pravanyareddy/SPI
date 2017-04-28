import RPi.GPIO as GPIO
import time
import random
import getpass
import MFRC522
import signal
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
x=0
while(x==0):
          GPIO.output(35, 0)
#          lcd_string("  CYCLE  UNLOCKED   ",LCD_LINE_1,2)
	  print "Cycle Unlocked"
#          lcd_string("                    ",LCD_LINE_2,2)
#          lcd_string("                    ",LCD_LINE_3,2)
#          lcd_string("                    ",LCD_LINE_4,2)
	  time.sleep(2)
          GPIO.output(38, 1)
	  print "on1"
          time.sleep(0.5)
          GPIO.output(38, 0)
	  print "off1"
          time.sleep(0.5)
          GPIO.output(38, 1)
	  print "on2"
          time.sleep(0.5)
          GPIO.output(38, 0)
	  print "off2"
          GPIO.output(35, 1)
          x+=1
