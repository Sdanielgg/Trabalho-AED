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

tree = ttk.Treeview(home, selectmode="browse", columns=("Name","Category"), show="headings", height=20)

style = ttk.Style()
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) 
style.configure("Treeview.Heading", font=('Comic Sans MS', 13)) 
style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 

tree.column("Name", width=140,anchor="center")
tree.heading("Name",text="Name")
tree.column("Description", width=250,anchor="center")
tree.heading("Description",text="Description")
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

#Buttons

userButton=Button(home,text="User",font=11,width=20,height=2,bg="#D9D9D9")
userButton.place(x=101,y=21)

myphotosButton=Button(home,text="My Photos",font=11,width=20,height=2,bg="#D9D9D9")
myphotosButton.place(x=401,y=21)

logoutButton=Button(home,text="Log Out",font=11,width=20,height=2,bg="#D9D9D9")
logoutButton.place(x=701,y=21)

openAlbum=Button(home,text="Open Album",font=11,width=20,height=2,bg="#D9D9D9")
openAlbum.place(x=101,y=460)

def load_categories():
    categories = []
    f_categories = open("files\\categories.txt", "r", encoding="utf-8")
    lines = f_categories.readlines()
    f_categories.close()
    for line in lines:
        content = line.strip().split(";")
        categories.append(content[0])
    f_categories.close()
    return categories

# Categories
categories = load_categories()
value_inside = StringVar()
value_inside.set("Filtrar")

genreSelect = OptionMenu(home, value_inside, *categories)
genreSelect.place(x=101,y=250)

home.mainloop()