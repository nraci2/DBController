import time
from configparser import ConfigParser

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
        
# To activate main relay    
   
    def powermain(self):
        pass
    
# To activate up relay    
    
    def powerup(self):
        pass
    
# To activate down relay

    def powerdown(self):
        pass
    
# EPO Behavior function (what happens when you epo)

    def epo(self):
        pass
    
    
    
    
    