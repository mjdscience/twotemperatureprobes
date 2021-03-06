import gspread
from oauth2client.service_account import ServiceAccountCredentials
from w1thermsensor import W1ThermSensor 
import datetime
import time

#Login information for Google Sheets using gspread 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sheet = client.open("").sheet1 #Name of sheet between the quotes (ie "2Temp")

#Sensors.  You need the serial numbers of the sensors from /sys/bus/w1/devices
#The serial numbers are 28-xxxxxx.  Put the part after the 28- in the quotes in the lines below.
sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "") #First sensor
sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "") #Second sensor

def elapse_time(): #counts time in seconds
  nowTime = datetime.datetime.now()
  seconds = nowTime - startTime
  seconds = int(seconds.total_seconds())
  return seconds

#infinite loop to get elapsed time and temperature and append them to a Google Sheet
while True:
  nowTime = datetime.dateime.now()
  elapse_time()
  T1 = sensor1.get_temperature()
  T2 = sensor2.get_temperature()
  values = [seconds,T1, T2]
  sheet.append_row(values)
  time.sleep(60)
