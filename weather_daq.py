import time
import adafruit_bme680
import board

start_time = time.time()
print(start_time)

while (time.time()-start_time) < 20:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)

    data = [time.time(), bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure]
    print(data)
    time.sleep(1)
