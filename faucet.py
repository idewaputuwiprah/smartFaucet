import RPi.GPIO as GPIO

class Faucet:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.IN) #==sets GPIO12 as INPUT sensor tutup
        GPIO.setup(16, GPIO.IN) #==sets GPIO16 as INPUT sensor buka
        GPIO.setup(20, GPIO.OUT) #==sets GPIO20 as OUTPUT H-Bridge
        GPIO.setup(21, GPIO.OUT) #==sets GPIO21 as OUTPUT H-Bridge

    def open_faucet(self):
        GPIO.output(20, True) #==  mengirimkan biner 1 ke pin GPIO 20 (membuka keran)
        GPIO.output(21, False) #== mengirim biner 0 ke pin GPIO 21 (membuka keran)

    def close_faucet(self):
        GPIO.output(20, False) #==  mengirimkan biner 1 ke pin GPIO 20 (menutup keran)
        GPIO.output(21, True) #== mengirim biner 0 ke pin GPIO 21 (menutup keran)

    def off_motor(self):
        GPIO.output(20, True) #==  mengirimkan biner 1 ke pin GPIO20 (power motor off)
        GPIO.output(21, True) #== mengirim biner 0 ke pin GPIO 21 (power motor off)

    
