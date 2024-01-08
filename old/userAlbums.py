from tkinter import *
from tkinter import ttk

userAlbums=Tk()

screenWidth = userAlbums.winfo_screenwidth()
screenHeight = userAlbums.winfo_screenheight()

appWidth = 1000
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

userAlbums.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
userAlbums.resizable(0,0)

#tree view and buttons 
deleteButton=Button()
addButton=Button()
myAlbums=ttk.Treeview(selectmode="browse",columns=("Name","Description","Category"),show="headings",height=10)
myAlbums.column("Description",width=140,anchor="center")
myAlbums.heading("Description",text="Description")

myAlbums.column("Category",width=140,anchor="center")
myAlbums.heading("Category",text="Category")

myAlbums.column("Name", width=140,anchor="center")
myAlbums.heading("Name",text="Name")


userAlbums.mainloop()