from tkinter import *
from tkinter import ttk

class Home(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.load_albums()
        self.userLoad()
#Functions
    def myAlbums(self):
        self.master.destroy()
<<<<<<< HEAD
        import myAlbumPhotos
        myAlbumPhotos.main()
=======
        import userAlbums
>>>>>>> 587cec652cddedc2e36f8e72a774c561540ad88f

    def logout(self):
        f=open("files\\users.txt", "r", encoding="utf-8")
        f.close()
<<<<<<< HEAD
=======
        lines = f.readlines()
>>>>>>> 587cec652cddedc2e36f8e72a774c561540ad88f
        for i, line in enumerate(lines):
            content = line.split(";")
            content[3] = "NotLogged"
            lines[i] = ";".join(content)
        f=open("files\\users.txt", "w", encoding="utf-8") 
        f.writelines(lines)
        f.close()
        self.master.destroy()
        import signIn
<<<<<<< HEAD
        signIn.main()
    def userLoad(self):
        f=open("files\\users.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close()
        for line in lines:
            content=line.split(";")
            if  (content[3]=="Logged"):
                self.userButton.config(text=content[0])
=======
>>>>>>> 587cec652cddedc2e36f8e72a774c561540ad88f

    def load_albums(self):
        f=open("files\\AlbumList.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close()
        for line in lines:
            content=line.strip().split(";")
            self.tree.insert('', 'end', values=(content[0],content[1],content[3]))

    def load_categories(self):
        categories = []
        f_categories = open("files\\categories.txt", "r", encoding="utf-8")
        lines = f_categories.readlines()
        f_categories.close()
        for line in lines:
            content = line.strip().split(";")
            categories.append(content[0])
        return categories

    def open_Album(self):
        selected = self.tree.selection()[0]
        currentItem = self.tree.focus()
        albumName = self.tree.item(currentItem, "values")[0]
        f=open("files\\Album.txt","w",encoding="utf-8")
        f.writelines(albumName)
        f.close()
        self.master.destroy()
        import album

#Tree view de albums
    def create_widgets(self):
        self.tree = ttk.Treeview(self, selectmode="browse", columns=("Name","Category","User"), show="headings", height=20)

        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) 
        style.configure("Treeview.Heading", font=('Comic Sans MS', 13)) 
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 

        self.tree.column("Name", width=150,anchor="center")
        self.tree.heading("Name",text="Name")
        self.tree.column("Category", width=150,anchor="center")
        self.tree.heading("Category",text="Category")
        self.tree.column("User", width=150,anchor="center")
        self.tree.heading("User",text="User")
        self.tree.place(x=400,y=100)
        #Buttons
        userButton=Button(self,text="User",font=11,width=20,height=2,bg="#D9D9D9")
        userButton.place(x=101,y=21)

        myphotosButton=Button(self,text="My Albums",font=11,width=20,height=2,bg="#D9D9D9",command=self.myAlbums)
        myphotosButton.place(x=401,y=21)

        logoutButton=Button(self,text="Log Out",font=11,width=20,height=2,bg="#D9D9D9",command=self.logout)
        logoutButton.place(x=701,y=21)

        openAlbum=Button(self,text="Open Album",font=11,width=20,height=2,bg="#D9D9D9",command=self.open_Album)
        openAlbum.place(x=101,y=460)
        # Categories
        categories = self.load_categories()
        value_inside = StringVar()
        value_inside.set("Filter")

        genreSelect = OptionMenu(self, value_inside, *categories)
        genreSelect.place(x=101,y=250)


def main():
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

    home_page = Home(master=home)
    home_page.pack(expand=True, fill="both")
    home.mainloop()
<<<<<<< HEAD
=======



>>>>>>> 587cec652cddedc2e36f8e72a774c561540ad88f
main()