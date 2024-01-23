from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#funções

class Album(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.load_album()
        self.load_user()
        self.loadcomments()

    def load_user(self):
        f=open("files\\users.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close()
        user=""
        for line in lines:
            content=line.split(";")
            if  (content[3]=="Logged"):
                user=content[0]
                print(user)
        
        
    def load_albumName(self):
        f=open("files\\Album.txt","r",encoding="utf-8")
        lines=f.readlines()
        albumname=lines[0]
        f.close()
        return albumname

    def load_album(self):
        albumname=self.load_albumName()
        f=open("files\\AlbumList.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close
        self.page_title.config(text="Album Name: "+albumname)
        for line in lines:
            content = line.strip().split(";")
            if content[0] == albumname:
                num_elements = len(content)-5
                description=content[2]
                description_str=str(description)
                self.description_textbox.config(state='normal')
                self.description_textbox.delete(1.0, 'end')
                self.description_textbox.insert("insert",description_str)
                for i in range(num_elements):
                    self.tree.insert('', 'end', values=(content[5 + i]))
                    
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

    def loadcomments(self):
        albumname=self.load_albumName()
        f=open("files\\comments.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close()
        for line in lines:
            content=line.strip().split(";")
            if content[0]==albumname:
                self.comments.insert('', 'end', values=(content[1],content[2]))

    def comment(self):
        f=open("files\\users.txt","r",encoding="utf-8")
        lines=f.readlines()
        f.close
        for line in lines:
            content=line.strip().split(";")
            if content[3]=="Logged":
                user=content[0]
        f=open("files\\Album.txt","r",encoding="utf-8")
        lines=f.readlines()
        albumname=lines[0]
        f.close()
        text=self.commentEntry.get()

        print(user)
        f=open("files\\comments.txt","a",encoding="utf-8")
        line=str(albumname)+";"+str(user)+";"+str(text)+";\n"
        f.write(line)
        f.close()
        self.comments.delete(*self.comments.get_children())
        self.loadcomments()

    


        
    def create_widgets(self):

        #Page Title
        self.page_title=Label(self,text="",font=20)
        self.page_title.place(x=500,y=10)

        tree_title=Label(self,text="Photos",font=14)
        tree_title.place(x=600,y=60)

        #buttons
        homeButton=Button(self,text="Back",font=11,width=20,height=2,command=self.home)
        homeButton.place(x=10,y=10)
        openButton=Button(self,text="Open Photo",font=11,width=20,height=2,command=self.display_image)
        openButton.place(x=60,y=320)
        
        #Description
        description_Label=Label(self,text="Description",font=14)
        description_Label.place(x=10,y=100)
        self.description_textbox = Text(self, font=('Calibri', 11),state='normal',  width=40,height=10)
        self.description_textbox.place(x=10, y=130)

        #Tree view de albums

        self.tree = ttk.Treeview(self, selectmode="browse", columns=("PhotoName"), show="headings", height=20)

        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14)) 
        style.configure("Treeview.Heading", font=('Comic Sans MS', 13)) 
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 

        self.tree.column("PhotoName", width=300,anchor="center")
        self.tree.heading("PhotoName",text="Photo Name")
        self.tree.place(x=600,y=100)

        #comments Label/Entry/Button
        commentLabel=Label(self,text="Comment:",font=7)
        commentLabel.place(x=10,y=650)
        self.commentEntry=Entry(self, width=25,font=11)
        self.commentEntry.place(x=110,y=650)
        self.button=Button(self,text="Comment",width=10,command=self.comment)
        self.button.place(x=350,y=650)

        #comments
        self.comments = ttk.Treeview(self, selectmode="browse", columns=("User","Comment"), show="headings", height=10)

        self.comments.column("User", width=150,anchor="center")
        self.comments.heading("User",text="User")
        self.comments.column("Comment", width=300)
        self.comments.heading("Comment",text="Comment")
        self.comments.place(x=10,y=400)

        #
        self.photoCanvas=Canvas(self,width=200,height=200,bg="gray")
        self.photoCanvas.place(x=950,y=200)
        

def main():
    album = Tk()
    album.configure(bg="#27544C")
    album.title("Album")
    appWidth = 1300
    appHeight = 700 
    screenWidth = album.winfo_screenwidth()
    screenHeight = album.winfo_screenheight()
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    album.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    user_album_page = Album(master=album)
    user_album_page.pack(expand=True, fill="both")
    album.mainloop()
main()