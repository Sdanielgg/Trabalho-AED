from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class addAlbumPopUp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.load_users()
        self.load_categories()
    # Functions
    def load_users(self):
        f=open("files\\users.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close()
        for line in lines:
            content=line.strip().split(";")
            if (content[3]=="Logged"):
                user=content[0]
                return user
    def goBack(self):
        self.master.destroy()
        import userAlbums
        userAlbums.main()

    def load_categories(self):
        categories = []
        f = open("files\\categories.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        for line in lines:
            content = line.strip().split(";")
            categories.append(content[0])
        f.close()
        return categories

    def addAlbum(self):
        user=self.load_users()
        AlbumName=self.txt_AlbumName.get()
        Description=self.description.get()
        Category=self.value_inside.get()
        f = open("files\\AlbumList.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        for line in lines:
            content=line.strip().split(";")
            if (content[0]==AlbumName):
                messagebox.showerror(title="Album Name in use",message="That Album Name is already in use, please choose another one!")
                return
        newLine= AlbumName+";"+Category +";"+Description+";"+user+";"+ "0"+";"+"\n"
        f = open("files\\AlbumList.txt", "a", encoding="utf-8")
        f.write(newLine)
        f.close()

    def create_widgets(self):
        # Go back Button
        go_Back = Button(text="Go Back", width=15, font=11,command=self.goBack)
        go_Back.place(x=10,y=10)

        # Album Name
        label_AlbumName = Label(text="Album Name:", font=14)
        label_AlbumName.place(x=30,y=120)

        self.txt_AlbumName = Entry(width=19, font=14)
        self.txt_AlbumName.place(x=155,y=120)

        # Categories
        categories = self.load_categories()
        self.value_inside = StringVar()
        self.value_inside.set("Select a Category")

        genreSelect = OptionMenu(self, self.value_inside, *categories)
        genreSelect.place(x=40,y=200)

        # Album Description
        descriptionLabel = Label(text="Description",font=14)
        descriptionLabel.place(x=500,y=80)

        self.description = Entry( width=40, border=10, font=11)
        self.description.place(x=500,y=120)

        #
        addPhotoButton = Button(self, text="Create Album", font=11,command=self.addAlbum)
        addPhotoButton.place(x=820,y=410)

 # Window
def main():
    addAlbum = Tk()
    addAlbum.title("Add Album")
    addAlbum.resizable(0,0)
    appWidth = 1000
    appHeight = 500 
    screenWidth = addAlbum.winfo_screenwidth()
    screenHeight = addAlbum.winfo_screenheight()
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    addAlbum.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    user_addAlbum_page = addAlbumPopUp(master=addAlbum)
    user_addAlbum_page.pack(expand=True, fill="both")

    addAlbum.mainloop()

