from tkinter import *
from tkinter import ttk

#funções

class Album(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.load_album()

    def load_album(self):
        f=open("files\\Album.txt","r",encoding="utf-8")
        lines=f.readlines()
        albumname=lines[0]
        f.close()
        f=open("files\\AlbumList.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close
        self.page_title.config(text=albumname)
        for line in lines:
            content = line.strip().split(";")
            if content[0] == albumname:
                num_elements = len(content)-4
                description=content[2]
                description_str=str(description)
                self.description_textbox.config(state='normal')
                self.description_textbox.delete(1.0, 'end')
                self.description_textbox.insert("insert",description_str)
                for i in range(num_elements):
                    self.tree.insert('', 'end', values=(content[4 + i]))
                    

    def line_len(self):
        f=open("files\\AlbumList.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close
        for line in lines:
            content=line.strip().split(";")
            print(len(content))
    def home(self):
        self.master.destroy()
        import home
        home.main()

    #window
    
    def create_widgets(self):

        #Page Title
        self.page_title=Label(self,text="Album title",font=20)
        self.page_title.place(x=500,y=10)

        tree_title=Label(self,text="Photos",font=14)
        tree_title.place(x=600,y=60)

        homeButton=Button(self,text="Back",font=11,width=20,height=2,command=self.home)
        homeButton.place(x=10,y=10)
        openButton=Button(self,text="Open Photo",font=11,width=20,height=2)
        openButton.place(x=110,y=420)
        
        #Description
        description_Label=Label(self,text="Description",font=14)
        description_Label.place(x=10,y=100)
        self.description_textbox = Text(self, font=('Calibri', 11),state='disabled',  width=40,height=10)
        self.description_textbox.place(x=10, y=130)

        #Tree view de albums

        self.tree = ttk.Treeview(self, selectmode="browse", columns=("PhotoName"), show="headings", height=20)

        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14)) 
        style.configure("Treeview.Heading", font=('Comic Sans MS', 13)) 
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 

        self.tree.column("PhotoName", width=300,anchor="center")
        self.tree.heading("PhotoName",text="Photo Name")
        self.showPasswordIcon = Button(self, image=self.eyeIconHidden, width=20, height=20, command=self.toggle_password_visibility)
        self.showPasswordIcon.place(x=500, y=70)


def main():
    album = Tk()
    album.configure(bg="#27544C")
    album.title("Album")
    appWidth = 1000
    appHeight = 600 
    screenWidth = album.winfo_screenwidth()
    screenHeight = album.winfo_screenheight()
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    album.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    user_album_page = Album(master=album)
    user_album_page.pack(expand=True, fill="both")
    album.mainloop()

main()

