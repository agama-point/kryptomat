# var/lib/mpd/playlists
# simple library for raspberry pi + serialdisplay (arduino) 
# 2016/05
# 2016/10 - GPIO Jmp
# octopusengine.org
# ------------------------------
import sys, os, subprocess, time
from socket import gethostname, gethostbyname #getIp
from time import sleep

  

# ======uart tft serial monitor / nextion===== 9600 / 115200
import serial
s = serial.Serial(port='/dev/ttyS0',baudrate=9600,                                                   
            timeout=3.0,
            xonxoff=False, rtscts=False, 
            writeTimeout=3.0,
            dsrdtr=False, interCharTimeout=None)
# timeout=1.0, bylo 3 ---9600
# co="bauds=115200"
# neXcmd(co)             
# ===============================================

#---nextion 2015/12-
  #simple label (similar arduino test)
def neXcmd(co):
    #s.write("t0.txt=")
    #s.write(chr(0x22))    
    s.write(co)
    #s.write(chr(0x22))
    s.write(chr(0xff))
    s.write(chr(0xff))
    s.write(chr(0xff))
    #s.write("\n")
    #displLab("testLAB raspi 2 " + ver)
    #def n(co):
    #hh.dispWrite(chr(co))
    time.sleep(0.001)

def neXtxt(kam,label):
    #s.write("t0.txt=")
    s.write(kam)
    s.write(".txt=")
    s.write(chr(0x22))
    #s.write("testLAB2")
    s.write(label)
    s.write(chr(0x22))
    s.write(chr(0xff))
    s.write(chr(0xff))
    s.write(chr(0xff))
    #s.write("\n")
    #displLab("testLAB raspi 2 " + ver)
    #def n(co):
    #hh.dispWrite(chr(co))
    time.sleep(0.05)  



#-------------------------end --------------
