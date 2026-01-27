import time
import board
import adafruit_bme680

i2c = board.I2C()
bme = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x77)

bme.sea_level_pressure = 1013.25

print("Warming up BME680...")
time.sleep(10)

while True:
    print(
        f"T={bme.temperature:.2f}C  "
        f"RH={bme.humidity:.2f}%  "
        f"P={bme.pressure:.2f}hPa  "
        f"G={bme.gas}Ω"
    )
    time.sleep(2)

# Not hit CTRL + C to quit