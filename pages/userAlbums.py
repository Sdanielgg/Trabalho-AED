from tkinter import *
from tkinter import ttk

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

#Page Title
title=Label(album,text="Make a button here to go back to home",font=11,bg="#D9D9D9")
title.place(x=0,y=0)

removeButton=Button(album,text="Remove Album",font=11,width=20,height=2,bg="#D9D9D9")
removeButton.place(x=110,y=220)

addButton=Button(album,text="Add Album",font=11,width=20,height=2,bg="#D9D9D9")
addButton.place(x=110,y=320)
openButton=Button(album,text="Open Album",font=11,width=20,height=2,bg="#D9D9D9")
openButton.place(x=110,y=420)

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




album.mainloop()