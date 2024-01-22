#Barrinha em cima com os diversos caminhos(dashboard, notificações, logout), na parte principal vai ter
from tkinter import *

import tkinter as tk

home=Tk()
screenWidth = home.winfo_screenwidth()
screenHeight = home.winfo_screenheight()

appWidth = 1000
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

home.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
home.title("Home")
home.resizable(0,0)

def button_click():
    print("O botão foi clicado!")

button = tk.Button(text="Click me!", command=button_click)

button.pack()

home.mainloop()
