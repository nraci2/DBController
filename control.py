import time
import threading

moving = False


def moving_up():
    while moving:
        time.sleep(.5)
        print("Moving up!")


def command_up():
    print("Commanded up!")
    global moving
    if not moving:
        moving = True
        t = threading.Thread(target=moving_up)
        t.start()


def stop():
    global moving
    if moving:
        moving = False
        print("STOP!")

