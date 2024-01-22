#Barrinha em cima com os diversos caminhos(dashboard, notificações, logout), na parte principal vai ter
from tkinter import *

import tkinter as tk
from tkinter import ttk

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

album=Tk()  
album.resizable(0,0)
album.configure(bg="#D9D9D9")
screenWidth = album.winfo_screenwidth()
screenHeight = album.winfo_screenheight()

appWidth =1000
appHeight = 600 

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

album.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

#Tree view de albums

tree = ttk.Treeview(album, selectmode="browse", columns=("Name","Description","FileType"), show="headings", height=20)

style = ttk.Style()
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) 
style.configure("Treeview.Heading", font=('Comic Sans MS', 13)) 
style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 

tree.column("Name", width=140,anchor="center")
tree.heading("Name",text="Name")
tree.column("Description", width=250,anchor="center")
tree.heading("Description",text="Description")
tree.column("FileType", width=140,anchor="center")
tree.heading("FileType",text="FileType")
tree.place(x=400,y=100)

def button_click():
    print("Button clicked!")

#button

button = Button(home, text="Click Me!", command=button_click)
button.place(x=450, y=500)

album.mainloop()