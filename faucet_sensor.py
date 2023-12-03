import RPi.GPIO as GPIO

class FaucetSensor:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        #or to use the physical pin numbers (1-40) instead of GPIO number
        #GPIO.setmode(GPIO.BOARD)
        # setting up pins as I/O
        #== GPIO 12 (PIN 32) input sensor kondisi tutup ====
        #== GPIO 16 (PIN 36) input sensor kondisi buka  ====
        GPIO.setup(12, GPIO.IN) #sets GPIO12 as INPUT
        GPIO.setup(16, GPIO.IN) #sets GPIO16 as INPUT
        GPIO.setup(20, GPIO.OUT) #sets GPIO20 as OUTPUT
        GPIO.setup(21, GPIO.OUT) #sets GPIO21 as OUTPUT

    def read_sensor_data(self):
        aboveSensor = GPIO.input(12) # membaca kondisi pin GPIO12 sensor tutup (Biner)
        belowSensor = GPIO.input(16) #membaca kondisi pin GPIO16 sensor buka (Biner)
        return SensorOutput(aboveSensor, belowSensor)
    
class SensorOutput:
    
    def __init__(self, aboveSensor, belowSensor):
        self.aboveSensor = aboveSensor
        self.belowSensor = belowSensor
