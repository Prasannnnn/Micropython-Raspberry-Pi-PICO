import time
from machine import Pin, I2C
from i2c_lcd import I2cLcd

# Define I2C pins and address
I2C_ADDR = 0x27
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# Initialize the LCD
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Define pins for the ultrasonic sensor
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

def get_distance():
    # Send a 10us pulse to trigger the measurement
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()

    # Measure the time for the echo signal
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()

    pulse_duration = time.ticks_diff(pulse_end, pulse_start)

    # Calculate distance in centimeters
    distance = (pulse_duration * 0.0343) / 2

    return distance

# Main loop
while True:
    distance = get_distance()
    print("Distance: {:.2f} cm".format(distance))
    lcd.clear()
    lcd.putstr("Distance:\n{:.2f} cm".format(distance))
    time.sleep(1)
