import tkinter as tk
from tkinter import ttk

# Creating Main App

app = tk.Tk()
app.title("DBController")
app.geometry("800x600")

# Buttons

up_button = ttk.Button(
    app,
    text="UP",
)
up_button.pack()


stop_button = ttk.Button(
    app,
    text="STOP"
)
stop_button.pack()


down_button = ttk.Button(
    app,
    text="DOWN"
)
down_button.pack()


# App Main Loop
app.mainloop()



