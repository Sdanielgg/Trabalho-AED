from tkinter import *
from tkinter import ttk

#funções
def line_len():
    f=open("files\\AlbumList.txt","r",encoding="utf-8")
    lines=f.readlines()
    list=[]
    f.close
    for line in lines:
        content=line.strip().split(";")
        print(len(content))
def home():
    album.destroy()
    import home
line_len()
#window
album=Tk()  
album.resizable(0,0)
album.configure(bg="#27544C")
screenWidth = album.winfo_screenwidth()
screenHeight = album.winfo_screenheight()

appWidth =1000
appHeight = 600 

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

album.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

#Page Title
title=Label(album,text="selectedAlbum",font=14,bg="#27544C")
title.place(x=600,y=60)

homeButton=Button(album,text="Back",font=11,width=20,height=2,command=home)
homeButton.place(x=10,y=10)
openButton=Button(album,text="Open Photo",font=11,width=20,height=2)
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