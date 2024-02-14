import time
import adafruit_pm25
import csv

meta_data = ["Time","PM1","PM2.5","PM10"]

file = open("air_quality_data.csv","w",newline='')

data_writer = csv.writer(file)
data_writerrow(meta_data)

start_time = time.time()
run_time = 30 # run for 30s
now = start_time

while now <= (start_time + run_time):
    now = time.time()
    aqdata = pm25.read()
    data = [now,aqdata["pm25 standard"],aqdata["pm25 standard"],aqdata["pm100 standard"]]
    data_writer.writerow(data)
    time.sleep(1)



