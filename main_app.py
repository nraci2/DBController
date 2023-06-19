import tkinter as tk
from tkinter import ttk
from drawbridge_control import Drawbridge
from power_control import Power

# Creating Main App

app = tk.Tk()
app.title("DBController")

# Defining Drawbridge object

Bridge = Drawbridge(False, False, False, False)
Pwr = Power(False, False, False, False)


# Defining function for app opening
def on_app_opening():
    Pwr.setdownoff()
    Pwr.setupoff()
    Pwr.setmainon()


# Defining function for app close
def on_app_closing():
    Bridge.stop()
    Pwr.off()
    app.destroy()



#  UP Button

up_button = ttk.Button(
    app,
    text="UP",
    command=lambda: [Bridge.commandup(), downdisable()]
)
up_button.grid(
    row=1,
    column=1,
    ipady=50,
    ipadx=125,
    sticky=""
    
)

# STOP Button

stop_button = ttk.Button(
    app,
    text="STOP",
    command=lambda: [Bridge.stop(), allenable()]

)
stop_button.grid(
    row=2,
    column=1,
    ipady=50,
    ipadx=125,
    sticky=""
)

# DOWN Button

down_button = ttk.Button(
    app,
    text="DOWN",
    command=lambda: [Bridge.commanddown(), updisable()]

)
down_button.grid(
    row=3,
    column=1,
    ipady=50,
    ipadx=125,
    sticky=""
)

# GetState Button

getstate_button = ttk.Button(
    app,
    text="Get State",
    command=Bridge.getstate

)
getstate_button.grid(
    row=1,
    column=2,
    sticky=""
)


def downdisable():
    down_button.configure(state="disable")


def updisable():
    up_button.configure(state="disable")


def allenable():
    up_button.configure(state="enable")
    down_button.configure(state="enable")


# START OF TESTING SECTION ##############################################################################

# Downlock Simulation

def setdl():
    Bridge.isdown = dlv.get()
    if Bridge.isdown:
        uplock_switch.configure(state="disable")
    else:
        uplock_switch.configure(state="normal")


dlv = tk.BooleanVar()

downlock_switch = ttk.Checkbutton(
    app,
    text="Downlock",
    variable=dlv,
    command=setdl,

)
downlock_switch.grid(
    row=2,
    column=2,
    sticky=""
)
# Uplock Simulation

def setul():
    Bridge.isup = ulv.get()
    if Bridge.isup:
        downlock_switch.configure(state="disable")
    else:
        downlock_switch.configure(state="normal")


ulv = tk.BooleanVar()

uplock_switch = ttk.Checkbutton(
    app,
    text="Uplock",
    variable=ulv,
    command=setul

)
uplock_switch.grid(
    row=3,
    column=2,
    sticky=""
)
# Uplock Simulation

def setfail():
    Bridge.isfailed = failv.get()


failv = tk.BooleanVar()

failed_switch = ttk.Checkbutton(
    app,
    text="Fail",
    variable=failv,
    command=setfail

)
#failed_switch.pack()

# Get Power IO config

powerio = ttk.Button(
    app,
    text="Power IO",
    command=Pwr.getio

)
powerio.grid(
    row=4,
    column=2,
    sticky=""
)
# Button to reset all relays to unpowered state

reset_button = ttk.Button(
    app,
    text="Reset Power to OFF",
    command=Pwr.off

)
reset_button.grid(
    row=5,
    column=2,
    sticky=""
)

exit_button = ttk.Button(
    app,
    text="EXIT",
    command=on_app_closing
)
exit_button.grid(
    row=6,
    column=2,
    sticky=""
)

# END OF TESTING SECTION ##############################################################################

# App Main Loop
#app.attributes('-fullscreen', True)
app.wait_visibility()
Pwr.setmainon()
app.protocol("WM_DELETE_WINDOW", on_app_closing)
app.mainloop()
