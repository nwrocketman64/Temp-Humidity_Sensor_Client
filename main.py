# Import the needed libraries.
from time import sleep_ms, ticks_ms
from machine import I2C, Pin

# Import the diver for the 1602 LCD.
from machine_i2c_lcd import I2cLcd

# Import the DHT library.
import dht

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

def main():
    """
    The main function for the program.
    """
    # Setup the the DHT11 Sensor.
    sensor = dht.DHT11(Pin(6))
    
    # Setup the 1602 LCD on pin GP8 (sda) and GP9 (scl)
    i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    
    # Init the screen.
    lcd.clear()
    lcd.backlight_on()
    lcd.display_on()
    
    # Put the startup message on the screen and wait for 5 seconds.
    lcd.putstr("Temp / Humidity\n     Sensor")
    sleep_ms(5000)
    
    # The main loop.
    while True:
        # Get measurements from the sensor.
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # Convert the temperature to fahenheit.
        f_temp = (temp * (9.0 / 5.0)) + 32.0
        
        # Clear the display and then display all the measurements.
        lcd.clear()
        lcd.putstr("Temp:{:.0f} F | {:.0f} C\nHumidity: {:.0f}%".format(f_temp, temp, hum))
        sleep_ms(2000)


# The program starts here.
if __name__ == "__main__":
    main()