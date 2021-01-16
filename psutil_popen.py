
import psutil
import time
from popen import Sh

while True:
  #cpu
  cpu_count = psutil.cpu_count()
  cpu_percent = psutil.cpu_percent(interval=1,percpu=True)
  cpu_freq = psutil.cpu_freq()

  #getloadavg
  loadavg = psutil.getloadavg()

  #memory
  virtual_memory = psutil.virtual_memory()

  #fan_speed
  fan = Sh('cat', '/sys/devices/pwm-fan/target_pwm')

  #AO-therm,CPU-therm,GPU-therm,PLL-therm,PMIC-Die,thermal-fan-est
  thermal_type = Sh('cat', '/sys/devices/virtual/thermal/thermal_zone*/type')
  thermal_temp = Sh('cat', '/sys/devices/virtual/thermal/thermal_zone*/temp')

  #disk
  disk =  psutil.disk_usage('/')

  print(cpu_freq)
  time.sleep(3)

