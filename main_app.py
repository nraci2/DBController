import tkinter as tk
from tkinter import ttk
from drawbridge_control import Drawbridge

# Defining Drawbridge object

Bridge = Drawbridge(False, False, False, False)

# Creating Main App

app = tk.Tk()
app.title("DBController")
app.geometry("250x200")


# Defining function for window close
def on_closing():
    Bridge.stop()
    app.destroy()


# Buttons

up_button = ttk.Button(
    app,
    text="UP",
    command=Bridge.commandup
)
up_button.pack()

stop_button = ttk.Button(
    app,
    text="STOP",
    command=Bridge.stop

)
stop_button.pack()

down_button = ttk.Button(
    app,
    text="DOWN",
    command=Bridge.commanddown

)
down_button.pack()

getstate_button = ttk.Button(
    app,
    text="Get State",
    command=Bridge.getstate

)
getstate_button.pack()


# START OF TESTING SECTION

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

downlock_switch.pack()


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
uplock_switch.pack()


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
failed_switch.pack()

# END OF TESTING SECTION

# App Main Loop
app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
