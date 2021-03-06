
import re
import os
import serial
import time

port = '/dev/ttyUSB0' # note I'm using Mac OS-X
ard = serial.Serial(port,115200,timeout=3,
           parity=serial.PARITY_NONE,
           bytesize=serial.EIGHTBITS,
           stopbits=serial.STOPBITS_ONE)
time.sleep(2)

def readline():
  while True:
    try:
       incoming = ard.readline().decode('ascii')
       print(incoming)
       ard.flush()
       if  "Received" in incoming :
         s=re.findall("\d+",incoming)[0]
         print(s)
         oscmd_1="sh -c 'echo "
         oscmd_2="> /sys/devices/pwm-fan/target_pwm'"
         os.system(oscmd_1+str(s)+oscmd_2)
    except:
       pass

if __name__ == '__main__' :
     readline()
