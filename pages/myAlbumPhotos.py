from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class AlbumPhotos(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.load_albums()

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
            
    def load_albums(self):
        user=self.load_users()
        print(user)
        f=open("files\\AlbumList.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close()
        for line in lines:
            content=line.strip().split(";")
            if(user==content[3]):
                self.tree.insert('', 'end', values=(content[0],content[1],content[2]))
        del lines

    def deleteSelected(self):
        selected = self.tree.selection()[0]
        currentItem = self.tree.focus()
        name = self.tree.item(currentItem, "values")[0]
        f=open("files\\AlbumList.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
        new_lines = []
        for line in lines:
            content = line.split(";")
            if content[0] != name:
                 new_lines.append(line)
        f=open("files\\AlbumList.txt", "w", encoding="utf-8")
        f.writelines(new_lines)
        f.close()
        self.tree.delete(selected)
        del lines
        del new_lines
        del content

    def addPhotoPopUp(self):
        self.master.destroy()
        import addPhotoPopUp
        addPhotoPopUp.main()
    
    def goToHome(self):
        self.master.destroy()
        import home
        home.main()
    
    def create_widgets(self):
        #treeview
        self.tree = ttk.Treeview(self, selectmode="browse", columns=("Name","Category"), show="headings", height=20)
        self.tree.column("Name", width=250,anchor="center")
        self.tree.heading("Name",text="Name")
        self.tree.column("Category", width=250,anchor="center")
        self.tree.heading("Category",text="Category")
        self.tree.place(x=400,y=100)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) 
        style.configure("Treeview.Heading", font=('Comic Sans MS', 13)) 
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        #buttons
        homeButton=Button(self,text="Home",font=11,width=20,height=2,bg="#D9D9D9",command=self.goToHome)
        homeButton.place(x=10,y=10)

        removeButton=tk.Button(self,text="Remove Photo",font=11,width=20,height=2,bg="#D9D9D9",command=self.deleteSelected)
        removeButton.place(x=110,y=220)

        addButton=tk.Button(self,text="Add Photo",font=11,width=20,height=2,bg="#D9D9D9",command=self.addPhotoPopUp)
        addButton.place(x=110,y=320)

        openButton=tk.Button(self,text="Open Album",font=11,width=20,height=2,bg="#D9D9D9")
        openButton.place(x=110,y=420) 

        
def main():
    album = tk.Tk()
    album.configure(bg="#D9D9D9")
    album.title("My Albums")
    appWidth = 1000
    appHeight = 600 
    screenWidth = album.winfo_screenwidth()
    screenHeight = album.winfo_screenheight()
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    album.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    user_album_page = AlbumPhotos(master=album)
    user_album_page.pack(expand=True, fill="both")

    album.mainloop()

