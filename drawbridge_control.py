import time
import threading
from power_control import Power

Pwr = Power(False, False, False, False)


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

                if self.ismoving:
                    time.sleep(0.5)
                    Pwr.setupon()
                    print("In transit(Up): " + str(self.ismoving))

            Pwr.setupoff()
            self.ismoving = False

            if self.isup:
                print("Uplock: " + str(self.isup))

        if not self.ismoving and not self.isup:
            self.ismoving = True
            t = threading.Thread(target=moveup)
            t.start()

    # Drawbridge Stop Method
    def stop(self):
        if self.ismoving:
            self.ismoving = False
            Pwr.setupoff()
            Pwr.setdownoff()
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

                if self.ismoving:
                    time.sleep(0.5)
                    Pwr.setdownon()
                    print("In Transit(Down): " + str(self.ismoving))


            Pwr.setdownoff()
            self.ismoving = False

            if self.isdown:
                print("Downlock: " + str(self.isdown))


        if not self.ismoving and not self.isdown:
            self.ismoving = True
            t = threading.Thread(target=movedown)
            t.start()
