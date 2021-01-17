
import psutil
import time
import subprocess 
import os

total_info = {}

while True:
  #cpu
  cpu_usage = psutil.cpu_percent(interval=1,percpu=True)
  cpu_freq = psutil.cpu_freq()

  for i in range(len(cpu_usage)):
    usage = { "cpu"+str(i+1) : cpu_usage[i] }
    total_info.update(usage)

  total_info.update({"cpu_freq" : cpu_freq[0]})

  #getloadavg 1,5,15m
  loadavg = psutil.getloadavg()
  total_info.update({"loadavg" : loadavg[2]})

  #memory
  mem = psutil.virtual_memory()
  total_info.update({"mem" : mem[2]})

  #gpu_usage
  gpu = subprocess.Popen(['cat', '/sys/devices/gpu.0/load'],stdout=subprocess.PIPE)
  gpu.wait()
  total_info.update({"gpu" : float(gpu.stdout.read())/10 })

  #fan_speed
  fan = subprocess.Popen(['cat', '/sys/devices/pwm-fan/target_pwm'],stdout=subprocess.PIPE)
  fan.wait()
  total_info.update({"fan" : int(fan.stdout.read()) })

  #AO-therm,CPU-therm,GPU-therm,PLL-therm,PMIC-Die,thermal-fan-est
  thermal_type = os.popen('cat /sys/devices/virtual/thermal/thermal_zone*/type')
  thermal_temp = os.popen('cat /sys/devices/virtual/thermal/thermal_zone*/temp')
  thermal_type_name = thermal_type.readlines()
  thermal_type_temp = thermal_temp.readlines()

  for i in range(len(thermal_type_name)):
     thermal_list = { str(thermal_type_name[i]).replace("\n","") : int(thermal_type_temp[i])/1000 }
     total_info.update(thermal_list)

  del total_info['PMIC-Die']

  #disk
  disk =  psutil.disk_usage('/')
  total_info.update({"disk" : disk[3] })

  print(total_info)

  time.sleep(5)
