#Barrinha em cima com os diversos caminhos(dashboard, notificações, logout), na parte principal vai ter
from tkinter import *
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
home.resizable(0,0)
home.configure(bg="#D9D9D9")
screenWidth = home.winfo_screenwidth()
screenHeight = home.winfo_screenheight()

appWidth =1000
appHeight = 600 

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

home.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

#Tree view de albums

tree = ttk.Treeview(home, selectmode="browse", columns=("Name","Description","FileType"), show="headings", height=20)

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

home.resizable(0,0)
home.configure(bg="#D9D9D9")
screenWidth = home.winfo_screenwidth()
screenHeight = home.winfo_screenheight()

appWidth =1000
appHeight = 600 

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

home.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

#Page Title
title=Label(home,text="selectedHome",font=11,bg="#D9D9D9")
title.place(x=0,y=0)


removeButton=Button(home,text="Remove Photo",font=11,width=20,height=2,bg="#D9D9D9")
removeButton.place(x=101,y=21)

addButton=Button(home,text="Add Photo",font=11,width=20,height=2,bg="#D9D9D9")
addButton.place(x=401,y=21)
openButton=Button(home,text="Open Photo",font=11,width=20,height=2,bg="#D9D9D9")
openButton.place(x=701,y=21)

openButton=Button(home,text="Open Photo",font=11,width=20,height=2,bg="#D9D9D9")
openButton.place(x=101,y=460)

home.mainloop()