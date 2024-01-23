from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk


class AlbumPhotos(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.load_album()

    def load_users(self):
        f = open("files\\users.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        for line in lines:
            content = line.strip().split(";")
            if (content[3] == "Logged"):
                user = content[0]
                return user
        del lines
            
    def load_album(self):
        f=open("files\\Album.txt","r",encoding="utf-8")
        lines=f.readlines()
        albumname=lines[0]
        f.close()
        f=open("files\\AlbumList.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close
        self.page_title.config(text="Album:"+albumname)
        for line in lines:
            content = line.strip().split(";")
            if content[0] == albumname:
                num_elements = len(content)-5
                for i in range(num_elements):
                    self.tree.insert('', 'end', values=(content[5 + i]))

    def deleteSelected(self):
        selected = self.tree.selection()[0]
        currentItem = self.tree.focus()
        name = self.tree.item(currentItem, "values")[0]
        f=open("files\\Album.txt","r",encoding="utf-8")
        lines=f.readlines()
        albumname=lines[0]
        f.close()
        f=open("files\\AlbumList.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        new_lines = []
        for line in lines:
            content = line.strip().split(";")
            if (content[0] == albumname):
                if name in line:
                    line = line.replace(name+ ";", "")
            new_lines.append(line)
        f=open("files\\AlbumList.txt", "w", encoding="utf-8")
        f.writelines(new_lines)
        f.close()
        self.tree.delete(selected)

    def addPhotoPopUp(self):
        self.master.destroy()
        import addPhotoPopUp
        addPhotoPopUp.main()
    
    def goToHome(self):
        self.master.destroy()
        import home
        home.main()

    def open_Album(self):
        currentItem = self.tree.focus()
        albumName = self.tree.item(currentItem, "values")[0]
        f=open("files\\Album.txt","w",encoding="utf-8")
        f.writelines(albumName)
        f.close()

    def display_image(self):
        currentItem = self.tree.focus()
        file_path = self.tree.item(currentItem, "values")[0]
        original_image = Image.open(file_path)
        aspect_ratio = original_image.width / original_image.height
        target_size = (200, int(200 / aspect_ratio))
        resized_image = original_image.resize(target_size, Image.ADAPTIVE)
        photo = ImageTk.PhotoImage(resized_image)
        self.photoCanvas.config(width=target_size[0], height=target_size[1])
        self.photoCanvas.create_image(0, 0, anchor=NW, image=photo)
        self.photoCanvas.image = photo

    def create_widgets(self):
        #page title
        self.page_title=Label(self,text="",font=14)
        self.page_title.place(x=300,y=10)

        #treeview
        self.tree = ttk.Treeview(self, selectmode="browse", columns=("PhotoName"), show="headings", height=20)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14)) 
        style.configure("Treeview.Heading", font=('Comic Sans MS', 13)) 
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 
        self.tree.column("PhotoName", width=300,anchor="center")
        self.tree.heading("PhotoName",text="Photo Name")
        self.tree.place(x=400,y=70)
        #buttons
        homeButton=Button(self,text="Home",font=11,width=20,height=2,bg="#D9D9D9",command=self.goToHome)
        homeButton.place(x=10,y=10)

        removeButton=tk.Button(self,text="Remove Photo",font=11,width=20,height=2,bg="#D9D9D9",command=self.deleteSelected)
        removeButton.place(x=110,y=220)

        addButton=tk.Button(self,text="Add Photo",font=11,width=20,height=2,bg="#D9D9D9",command=self.addPhotoPopUp)
        addButton.place(x=110,y=320)

        openButton=tk.Button(self,text="Open Photo",font=11,width=20,height=2,bg="#D9D9D9",command=self.display_image)
        openButton.place(x=110,y=420) 

        self.photoCanvas=Canvas(self,width=200,height=200,bg="gray")
        self.photoCanvas.place(x=900,y=200)

def main():
    album = tk.Tk()
    album.configure(bg="#D9D9D9")
    album.title("My Album's Photos")
    appWidth = 1300
    appHeight = 700 
    screenWidth = album.winfo_screenwidth()
    screenHeight = album.winfo_screenheight()
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    album.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    user_album_page = AlbumPhotos(master=album)
    user_album_page.pack(expand=True, fill="both")

    album.mainloop()