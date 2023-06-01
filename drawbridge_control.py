import time
import threading
from power_control import Power


class Drawbridge:

    def __init__(self, ismoving, isup, isdown, isfailed):
        self.ismoving = ismoving
        self.isup = isup
        self.isdown = isdown
        self.isfailed = isfailed

    def getstate(self):
        print("In transit: " + str(self.ismoving))
        print("Uplock: " + str(self.isup))
        print("Downlock: " + str(self.isdown))
        print("Failed: " + str(self.isfailed))

    # Drawbridge Up Command Method
    def commandup(self):

        print("Commanded up!")
        if self.ismoving:
            print("ERROR: BRIDGE IN TRANSIT!")
        elif self.isup:
            print("ERROR: BRIDGE IS ALREADY UP!")

        def moveup():
            while self.ismoving and not self.isup:
                time.sleep(.5)
                print("Moving up!")
                if self.isup:
                    print("Reached Uplock!")
                    self.ismoving = False

        if not self.ismoving and not self.isup:
            self.ismoving = True
            t = threading.Thread(target=moveup)
            t.start()

    # Drawbridge Stop Method
    def stop(self):
        if self.ismoving:
            self.ismoving = False
            print("STOP!")

    # Drawbridge Down Command Method
    def commanddown(self):

        print("Commanded down!")
        if self.ismoving:
            print("ERROR: BRIDGE IN TRANSIT!")
        elif self.isdown:
            print("ERROR: BRIDGE IS ALREADY DOWN!")

        def movedown():
            while self.ismoving and not self.isdown:
                time.sleep(.5)
                print("Moving down!")
                if self.isdown:
                    print("Reached Downlock!")
                    self.ismoving = False

        if not self.ismoving and not self.isdown:
            self.ismoving = True
            t = threading.Thread(target=movedown)
            t.start()
