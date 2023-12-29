from tkinter import *
from tkinter import ttk

album=Tk()  
album.geometry("1000x600")
album.resizable(0,0)
screenWidth = album.winfo_screenwidth()
screenHeight = album.winfo_screenheight()

appWidth =1000
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

album.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

#Page Title
title=Label(album,text="selectedAlbum",font=11)
title.place(x=0,y=0)

removeButton=Button(album,text="Remove Photo",font=11)
removeButton.place(x=400,y=100)

addButton=Button(album,text="Add Photo",font=11)
addButton.place()

tree = ttk.Treeview(album, selectmode="browse", columns=("Name","Description"), show="headings", height=10)
tree.column("Name", width=140,anchor="center")
tree.heading("Name",text="Name")

tree.column("Description", width=200,anchor="center")
tree.heading("Description",text="Description")
tree.column
tree.place(x=400,y=100)


album.mainloop()