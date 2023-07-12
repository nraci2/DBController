from configparser import ConfigParser
import RPi.GPIO as GPIO

# Importing GPIO config from rpi_io.ini

# Instantiate
config = ConfigParser()

# Parse Existing File
config.read('rpi_io.cfg')

# Read Values from file

main_pin = config.get('Relay_Module', 'main_pin')
up_pin = config.get('Relay_Module', 'up_pin')
down_pin = config.get('Relay_Module', 'down_pin')
epo_pin = config.get('EPO_Monitoring', 'epo_pin')
horn_light_pin = config.get('Relay_Module', 'horn_light_pin')

dw1_pin = config.get('DS/US_Monitoring', 'dw1_pin')
dw2_pin = config.get('DS/US_Monitoring', 'dw2_pin')
up1_pin = config.get('DS/US_Monitoring', 'up1_pin')
up2_pin = config.get('DS/US_Monitoring', 'up2_pin')

# Setting up GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(int(main_pin), GPIO.OUT)  # Main power setup
GPIO.setup(int(up_pin), GPIO.OUT)  # UP power setup
GPIO.setup(int(down_pin), GPIO.OUT)  # DOWN power setup
GPIO.setup(int(horn_light_pin), GPIO.OUT)  # Horn + Light power setup

GPIO.setup(int(dw1_pin), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Downswitch 1 input
GPIO.setup(int(dw2_pin), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Downswitch 2 input
GPIO.setup(int(up1_pin), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Upswitch 1 input
GPIO.setup(int(up2_pin), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Upswitch 2 input

# Setting Default Outputs to OFF
GPIO.output(int(main_pin), 1)
GPIO.output(int(up_pin), 1)
GPIO.output(int(down_pin), 1)
GPIO.output(int(horn_light_pin), 1)


# To get IO values in maintenance screen
def getio():
    print("Main " + main_pin)
    print("Up: " + up_pin)
    print("Down: " + down_pin)
    print("Horn+Light: " + horn_light_pin)
    print("EPO: " + epo_pin)


class LimitSwitches:

    def __init__(self, dw1, dw2, up1, up2):
        self.dw1 = dw1
        self.dw2 = dw2
        self.up1 = up1
        self.up2 = up2

    def get_dw1(self):
        if GPIO.input(int(dw1_pin)) == GPIO.HIGH:
            self.dw1 = True
            return
        elif GPIO.input(int(dw1_pin)) == GPIO.LOW:
            self.dw1 = False
            return

    def get_dw2(self):
        if GPIO.input(int(dw2_pin)) == GPIO.HIGH:
            self.dw2 = True
        elif GPIO.input(int(dw2_pin)) == GPIO.LOW:
            self.dw2 = False

    def get_up1(self):
        if GPIO.input(int(up1_pin)) == GPIO.HIGH:
            self.up1 = True
        elif GPIO.input(int(up1_pin)) == GPIO.LOW:
            self.up1 = False

    def get_up2(self):
        if GPIO.input(int(up2_pin)) == GPIO.HIGH:
            self.up2 = True
        elif GPIO.input(int(up2_pin)) == GPIO.LOW:
            self.up2 = False


class Power:

    def __init__(self, mainon, upon, downon, isepo, alloff, hornlighton):
        self.mainon = mainon
        self.upon = upon
        self.downon = downon
        self.isepo = isepo
        self.alloff = alloff
        self.hornlighton = hornlighton

    def getstate(self):
        print("Main ON: " + str(self.mainon))
        print("Up On: " + str(self.upon))
        print("Down On: " + str(self.downon))
        print("Is EPO: " + str(self.isepo))

    # To reset all relays to unpowered state

    def off(self):
        self.alloff = True
        print("Setting all relays to unpowered state.")
        GPIO.output(int(main_pin), 1)
        GPIO.output(int(up_pin), 1)
        GPIO.output(int(down_pin), 1)
        GPIO.output(int(horn_light_pin), 1)

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

    # To activate/deactivate horn+light
    def sethornlighton(self):
        GPIO.output(int(horn_light_pin), 0)
        self.hornlighton = True

    def sethornlightoff(self):
        GPIO.output(int(horn_light_pin), 1)
        self.hornlighton = False

    # EPO Behavior function (what happens when you epo)

    def epo(self):
        pass
