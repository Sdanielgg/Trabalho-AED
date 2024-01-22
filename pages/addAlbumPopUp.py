from tkinter import *
from tkinter import messagebox

# Functions
def load_users():
    f=open("files\\users.txt","r",encoding="utf-8")
    lines=f.readlines()
    f.close()
    for line in lines:
        content=line.strip().split(";")
        if (content[3]=="Logged"):
            user=content[0]
            return user

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

def addAlbum():
    user=load_users()
    AlbumName=txt_AlbumName.get()
    Description=description.get()
    Category=value_inside.get()
    f = open("files\\AlbumList.txt", "r", encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        content=line.strip().split(";")
        if (content[1]==AlbumName):
            messagebox.showerror(title="Album Name in use",message="That Album Name is already in use, please choose another one!")
            return
        
    f.close()
    newLine= AlbumName+";"+Category +";"+Description+";"+user+";"+";"+ "\n"
    f = open("files\\AlbumList.txt", "a", encoding="utf-8")
    f.write(newLine)
    f.close()

# Window
AlbumPopUp = Tk()
AlbumPopUp.configure(bg="grey")

screenWidth = AlbumPopUp.winfo_screenwidth()
screenHeight = AlbumPopUp.winfo_screenheight()

appWidth = 1000
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

AlbumPopUp.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

# Go back Button
go_Back = Button(text="Go Back", width=15, font=11)
go_Back.place(x=10,y=10)

# Album Name
label_AlbumName = Label(text="Album Name:", font=14, bg="grey")
label_AlbumName.place(x=30,y=120)

txt_AlbumName = Entry(width=19, font=14)
txt_AlbumName.place(x=155,y=120)

# Categories
categories = load_categories()
value_inside = StringVar()
value_inside.set("Select a Category")

genreSelect = OptionMenu(AlbumPopUp, value_inside, *categories)
genreSelect.place(x=40,y=200)

# Album Description
descriptionLabel = Label(text="Description",font=14, bg="grey")
descriptionLabel.place(x=500,y=80)

description = Entry( width=40, border=10, font=11)
description.place(x=500,y=120)

#
addPhotoButton = Button(AlbumPopUp, text="Create Album", font=11,command=addAlbum)
addPhotoButton.place(x=820,y=410)

AlbumPopUp.mainloop()
