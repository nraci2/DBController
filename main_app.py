import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from drawbridge_control import Drawbridge
import power_control
from power_control import Power
import threading
import time

### MAIN APP CREATION ###

app = tk.Tk()
app.title("DBController")
main_app_frame = Frame(app)
main_app_frame.pack(fill=tk.BOTH, expand=1)
status_labels_frame = Frame(app)
### DRAWBRIDGE AND POWER OBJECTS ###

Bridge = Drawbridge(False, False, False, False)
Pwr = Power(False, False, False, False, False, False)


### MONITORING LOOP ###
def set_label_states():
    down_label_var.set(str(Bridge.isdown))
    up_label_var.set(str(Bridge.isup))
    transit_label_var.set(str(Bridge.ismoving))


monloop = False


def stop_monitoring_loop():
    print("Attempting to close monitoring loop...")
    global monloop
    monloop = False


def monitoring_loop():
    global monloop
    print("Attempting to start monitoring loop...")

    def get_switch_states():
        global monloop
        print("Loop Started in thread")
        while monloop:
            time.sleep(0.1)
            if monloop:
                set_label_states()

        print("Loop broke in thread")

    if not monloop:
        monloop = True
        mon_t = threading.Thread(target=get_switch_states)
        mon_t.start()


### FUNCTIONS TO RUN ON APP OPENING ###
def on_app_opening():
    monitoring_loop()
    Pwr.setdownoff()
    Pwr.setupoff()
    Pwr.setmainon()


### FUNCTIONS TO RUN ON APP CLOSING ###
def on_app_closing():
    stop_monitoring_loop()
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
# Transit decorative label
transit_label = ttk.Label(
    status_labels_frame,
    text="BRIDGE IN TRANSIT: "
)
transit_label.grid(
    row=1,
    column=3
)
# Transit Status Label
transit_label_var = tk.StringVar()

transit_status_label = ttk.Label(
    status_labels_frame,
    textvariable=transit_label_var
)
transit_status_label.grid(
    row=1,
    column=4
)

# Upswitch decorative labels
up_label_S1 = ttk.Label(
    status_labels_frame,
    text="UPSWITCH1(S1): "
)
up_label_S1.grid(
    row=2,
    column=3,
    sticky="w"
)
# Upswitch status label
up_label_var = tk.StringVar()

up_status_label = ttk.Label(
    status_labels_frame,
    textvariable=up_label_var
)
up_status_label.grid(
    row=2,
    column=4,
)

# Downswitch decorative labels
down_label_S3 = ttk.Label(
    status_labels_frame,
    text="DOWNSWITCH1(S3): "
)
down_label_S3.grid(
    row=3,
    column=3,
)

# Downswitch status label
down_label_var = tk.StringVar()

down_status_label = ttk.Label(
    status_labels_frame,
    textvariable=down_label_var
)
down_status_label.grid(
    row=3,
    column=4,
)


### START OF TESTING SECTION ##############################################################################

# Downlock Simulation

def setdl():
    Bridge.isdown = dlv.get()
    if Bridge.isdown:
        uplock_switch.configure(state="disable")
    else:
        uplock_switch.configure(state="normal")


dlv = tk.BooleanVar()

downlock_switch = ttk.Checkbutton(
    main_app_frame,
    text="Downlock",
    variable=dlv,
    command=lambda: [setdl(), allenable()]

)
downlock_switch.grid(
    row=2,
    column=2,
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
    main_app_frame,
    text="Uplock",
    variable=ulv,
    command=lambda: [setul(), allenable()]

)
uplock_switch.grid(
    row=3,
    column=2,
)

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
