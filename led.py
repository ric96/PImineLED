import time
from mcpi import minecraft
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
flag=0
mc = minecraft.Minecraft.create()
mc.postToChat("Hello world")
pos = mc.player.getPos()
mc.postToChat("X:"+str(pos.x)+" Y:"+str(pos.y)+" Z:"+str(pos.z))



while True:
  blockEvent = mc.events.pollBlockHits()
  print blockEvent
  if blockEvent != []:
    if flag == 0:
      GPIO.output(11, True)
      print "ON"
      flag = 1

    elif flag == 1:
      print "OFF"
      GPIO.output(11, False)
      flag=0
  time.sleep(0.1)
