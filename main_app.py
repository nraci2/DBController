import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from drawbridge_control import Drawbridge
import power_control
from power_control import Power, LimitSwitches
import time
import threading


### MAIN APP CREATION ###

# Monitoring Class


class Monitoring:

    def __init__(self, state, abort):
        self.state = state
        self.abort = abort

    def stop(self):
        print("Attempting to close monitoring loop...")
        self.state = False
        self.abort = True

    def start(self):
        if self.state:
            print("Monitoring is already: " + str(self.state))

        def label_update_call():
            print("Loop Started in thread")

            while self.state:
                time.sleep(0.1)
                if not self.abort:
                    label_update()
                elif self.abort:
                    break

            print("Loop broke in thread. State = " + str(self.state) + " ABORT = " + str(self.abort))

        if not self.state:
            print("Attempting to start monitoring loop...")
            self.state = True
            mon_t = threading.Thread(target=label_update_call)
            mon_t.start()


### TKINTER WINDOW SETUP ###
app = tk.Tk()
app.title("DBController")
main_app_frame = Frame(app)
main_app_frame.pack(fill=tk.BOTH, expand=1)
status_labels_frame = Frame(app)

### DRAWBRIDGE, POWER AND MONITORING OBJECTS ###
Bridge = Drawbridge(False, False, False, False)
Pwr = Power(False, False, False, False, False, False)
LimSW = LimitSwitches(False, False, False, False)
Monitoring = Monitoring(False, False)


### LABEL UPDATE FUNCTION CALLED BY MONITORING CLASS
def label_update():
    downlock_label_var.set(str(Bridge.isdown))
    uplock_label_var.set(str(Bridge.isup))
    transit_label_var.set(str(Bridge.ismoving))
    monloop_label_var.set(str(Monitoring.state))

    LimSW.get_up1()
    up1_label_var.set(str(LimSW.up1))
    LimSW.get_up2()
    up2_label_var.set(str(LimSW.up2))
    LimSW.get_dw1()
    dw1_label_var.set(str(LimSW.dw1))
    LimSW.get_dw2()
    dw2_label_var.set(str(LimSW.dw2))


### FUNCTIONS TO RUN ON APP OPENING ###
def on_app_opening():
    Monitoring.start()
    Pwr.setdownoff()
    Pwr.setupoff()
    Pwr.setmainon()


### FUNCTIONS TO RUN ON APP CLOSING ###
def on_app_closing():
    Monitoring.stop()
    print("Waiting for monitoring loop to stop...")
    time.sleep(2)
    Bridge.stop()
    Pwr.off()
    app.destroy()


### CONTROL BUTTONS SETUP ###

#  UP Button

up_button = ttk.Button(
    main_app_frame,
    text="UP",
    command=lambda: [Bridge.commandup(), downdisable()]
)
up_button.grid(
    row=1,
    column=1,
    ipady=50,
    ipadx=125
)

# STOP Button

stop_button = ttk.Button(
    main_app_frame,
    text="STOP",
    command=lambda: [Bridge.stop(), allenable()]

)
stop_button.grid(
    row=2,
    column=1,
    ipady=50,
    ipadx=125
)

# DOWN Button

down_button = ttk.Button(
    main_app_frame,
    text="DOWN",
    command=lambda: [Bridge.commanddown(), updisable()]

)
down_button.grid(
    row=3,
    column=1,
    ipady=50,
    ipadx=125
)


### BUTTON DISABLING FUNCTIONS ###
# To prevent unintended activation of multiple relays at once

def downdisable():
    down_button.configure(state="disable")


def updisable():
    up_button.configure(state="disable")


def allenable():
    if not Bridge.ismoving:
        up_button.configure(state="enable")
        down_button.configure(state="enable")


### STATUS LABELS ###
# Monitoring loop decorative label
monloop_label = ttk.Label(
    status_labels_frame,
    text="MONITORING LOOP: "
)
monloop_label.grid(
    row=0,
    column=2,
    sticky="w"
)

# Monitoring loop status label
monloop_label_var = tk.StringVar()

monloop_status_label = ttk.Label(
    status_labels_frame,
    textvariable=monloop_label_var
)
monloop_status_label.grid(
    row=0,
    column=3,
    sticky="w"
)
# Transit decorative label
transit_label = ttk.Label(
    status_labels_frame,
    text="BRIDGE IN TRANSIT: "
)
transit_label.grid(
    row=1,
    column=2,
    sticky="w"
)

# Transit Status Label
transit_label_var = tk.StringVar()

transit_status_label = ttk.Label(
    status_labels_frame,
    textvariable=transit_label_var
)
transit_status_label.grid(
    row=1,
    column=3,
    sticky="w"
)

# Uplock decorative labels
uplock_label_S1 = ttk.Label(
    status_labels_frame,
    text="UPLOCK: "
)
uplock_label_S1.grid(
    row=2,
    column=2,
    sticky="w"
)
# Uplock status label
uplock_label_var = tk.StringVar()

uplock_status_label = ttk.Label(
    status_labels_frame,
    textvariable=uplock_label_var
)
uplock_status_label.grid(
    row=2,
    column=3,
    sticky="w"
)

# Downlock decorative labels
downlock_label_S3 = ttk.Label(
    status_labels_frame,
    text="DOWNLOCK: "
)
downlock_label_S3.grid(
    row=3,
    column=2,
    sticky="w"
)

# Downlock status label
downlock_label_var = tk.StringVar()
downlock_status_label = ttk.Label(
    status_labels_frame,
    textvariable=downlock_label_var
)
downlock_status_label.grid(
    row=3,
    column=3,
    sticky="w"
)

# Upswitch 1 decorative label
up1_label = ttk.Label(
    status_labels_frame,
    text="UPSWITCH1(S1): "
)
up1_label.grid(
    row=4,
    column=2,
    sticky="w"
)

# Upswitch 1 status label
up1_label_var = tk.StringVar()
up1_status_label = ttk.Label(
    status_labels_frame,
    textvariable=up1_label_var
)
up1_status_label.grid(
    row=4,
    column=3,
    sticky="w"
)

# Upswitch 2 decorative label
up2_label = ttk.Label(
    status_labels_frame,
    text="UPSWITCH2(S5): "
)
up2_label.grid(
    row=5,
    column=2,
    sticky="w"
)

# Upswitch 2 status label
up2_label_var = tk.StringVar()
up2_status_label = ttk.Label(
    status_labels_frame,
    textvariable=up2_label_var
)
up2_status_label.grid(
    row=5,
    column=3,
    sticky="w"
)

# Downswitch 1 decorative label
dw1_label = ttk.Label(
    status_labels_frame,
    text="DOWNSWITCH1(S3): "
)
dw1_label.grid(
    row=6,
    column=2,
    sticky="w"
)

# Downswitch 1 status label
dw1_label_var = tk.StringVar()
dw1_status_label = ttk.Label(
    status_labels_frame,
    textvariable=dw1_label_var
)
dw1_status_label.grid(
    row=6,
    column=3,
    sticky="w"
)

# Downswitch 2 decorative label
dw2_label = ttk.Label(
    status_labels_frame,
    text="DOWNSWITCH2(S4): "
)
dw2_label.grid(
    row=7,
    column=2,
    sticky="w"
)

# Downswitch 2 status label
dw2_label_var = tk.StringVar()
dw2_status_label = ttk.Label(
    status_labels_frame,
    textvariable=dw2_label_var
)
dw2_status_label.grid(
    row=7,
    column=3,
    sticky="w"
)


### START OF TESTING SECTION ##############################################################################


# Get Power IO config

powerio = ttk.Button(
    main_app_frame,
    text="Power IO",
    command=power_control.getio

)
powerio.grid(
    row=4,
    column=2,
)
# Button to reset all relays to unpowered state

reset_button = ttk.Button(
    main_app_frame,
    text="Reset Power to OFF",
    command=Pwr.off

)
reset_button.grid(
    row=5,
    column=2,
)

exit_button = ttk.Button(
    main_app_frame,
    text="EXIT",
    command=on_app_closing
)
exit_button.grid(
    row=6,
    column=2,
)

### END OF TESTING SECTION ##############################################################################

### APP FRAME SETUP ###
main_app_frame.grid(
    row=0,
    column=0,
    sticky="e"
)
status_labels_frame.grid(
    row=0,
    column=1,
    sticky="w",
)

# Row and Column growth setup for grids
main_app_frame.grid_rowconfigure(0, weight=1)
main_app_frame.grid_columnconfigure(0, weight=1)
status_labels_frame.grid_rowconfigure(0, weight=1)
status_labels_frame.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

### APP MAIN LOOP ###

# app.attributes('-fullscreen', True)
app.wait_visibility()
on_app_opening()
app.protocol("WM_DELETE_WINDOW", on_app_closing)
app.mainloop()
