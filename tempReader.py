#Program to print the temperatures in the terminal

from w1thermsensor import W1ThermSensor 
import datetime
import time
 
sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "") #First sensor - insert the probe name
sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "") #Second sensor - insert the probe name

def elapse_time(): #counts time in seconds
  nowTime = datetime.datetime.now()
  seconds = nowTime - startTime
  seconds = int(seconds.total_seconds())
  return seconds

#infinite loop to record the temperature once every minute
while True:
  nowTime = datetime.dateime.now()
  elapse_time()
  T1 = sensor1.get_temperature()
  T2 = sensor2.get_temperature()
  values = [seconds,T1, T2]
  print (seconds, T1, T2)
  sleep(60)
