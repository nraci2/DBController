from configparser import ConfigParser
import RPi.GPIO as GPIO

# Importing GPIO config from rpi_io.ini

# Instantiate
config = ConfigParser()

# Parse Existing File
config.read('rpi_io.cfg')

# Read Values from file

main_pin = config.get('Relay_Module', 'main_pin')
main_mode = config.get('Relay_Module', 'main_mode')

up_pin = config.get('Relay_Module', 'up_pin')
up_mode = config.get('Relay_Module', 'up_mode')

down_pin = config.get('Relay_Module', 'down_pin')
down_mode = config.get('Relay_Module', 'down_mode')

epo_pin = config.get('EPO_Monitoring', 'epo_pin')
epo_mode = config.get('EPO_Monitoring', 'epo_mode')

# Setting up GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(int(main_pin), GPIO.OUT)  # Main power setup
GPIO.setup(int(up_pin), GPIO.OUT)  # UP power setup
GPIO.setup(int(down_pin), GPIO.OUT)  # DOWN power setup


class Power:

    def __init__(self, mainon, upon, downon, isepo):
        self.mainon = mainon
        self.upon = upon
        self.downon = downon
        self.isepo = isepo

    def getstate(self):
        print("Main ON: " + str(self.mainon))
        print("Up On: " + str(self.upon))
        print("Down On: " + str(self.downon))
        print("Is EPO: " + str(self.isepo))

    def getio(self):
        print("Main " + main_pin + main_mode)
        print("Up: " + up_pin + up_mode)
        print("Down: " + down_pin + down_mode)
        print("EPO: " + epo_pin + epo_mode)

    # To reset all relays to unpowered state

    def off(self):
        print("Setting all relays to unpowered state.")
        GPIO.output(int(main_pin), 1)
        GPIO.output(int(up_pin), 1)
        GPIO.output(int(down_pin), 1)

    # To activate/deactivate main relay

    def setmainon(self):
        GPIO.output(int(main_pin), 0)
        self.mainon = True
        print("Main Relay ON!")

    def setmainoff(self):
        GPIO.output(int(main_pin), 1)
        self.mainon = False
        print("Main Relay OFF!")

    # To activate/deactivate up relay

    def setupon(self):
        GPIO.output(int(up_pin), 0)
        self.upon = True
        pass

    def setupoff(self):
        GPIO.output(int(up_pin), 1)
        self.upon = False
        pass

    # To activate/deactivate down relay

    def setdownon(self):
        GPIO.output(int(down_pin), 0)
        self.downon = True
        pass

    def setdownoff(self):
        GPIO.output(int(down_pin), 1)
        self.downon = False
        pass

    # EPO Behavior function (what happens when you epo)

    def epo(self):
        pass
