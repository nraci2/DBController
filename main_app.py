import tkinter as tk
from tkinter import ttk
import control
from control import moving


# Creating Main App

app = tk.Tk()
app.title("DBController")
app.geometry("250x100")

# Buttons

up_button = ttk.Button(
    app,
    text="UP",
    command=control.command_up
)
up_button.pack()

stop_button = ttk.Button(
    app,
    text="STOP",
    command=control.stop

)
stop_button.pack()

down_button = ttk.Button(
    app,
    text="DOWN",

)
down_button.pack()

# App Main Loop
app.mainloop()

