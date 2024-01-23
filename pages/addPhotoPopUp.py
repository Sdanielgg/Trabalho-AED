from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import messagebox

#Functions
class addPhotoPopUp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    def goBack(self):
        self.master.destroy()
        import myAlbumPhotos
        myAlbumPhotos.main()
        
    def open_image(self):
        self.file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.file_path:
            self.display_image(self.file_path)

    def add_Image(self):
        print(self.file_path)
        photoPath = self.file_path
        f = open("files\\Album.txt", "r", encoding="utf-8")
        AlbumName = f.readline().strip()
        f.close()
        print(AlbumName)
        f=open("files\\AlbumList.txt", "r", encoding="utf-8") 
        lines = f.readlines()
        f.close()
        photo_path_exists = False
        for i, line in enumerate(lines):
            content = line.strip().split(";")
            if content and content[0] == AlbumName:
                if photoPath.strip() in line:
                    photo_path_exists = True
                    messagebox.showerror(title="Photo duplicate found!",message="That photo already exists in the album!")
                else:
                    lines[i] = lines[i].rstrip() + photoPath + ";\n"
        if not photo_path_exists:
            f=open("files\\AlbumList.txt", "w", encoding="utf-8") 
            f.writelines(lines)
            f.close


    def display_image(self,file_path):
        # Open the image
        original_image = Image.open(file_path)

        aspect_ratio = original_image.width / original_image.height
        
        target_size = (300, int(300 / aspect_ratio))
        resized_image = original_image.resize(target_size, Image.ADAPTIVE)
        
        photo = ImageTk.PhotoImage(resized_image)
        
        self.photoCanvas.config(width=target_size[0], height=target_size[1])
        
        self.photoCanvas.create_image(0, 0, anchor=NW, image=photo)
        self.photoCanvas.image = photo

    def create_widgets(self):

        #Containers
        backCon=Frame(self)
        backCon.pack(side=TOP)
        container1=Frame(self)
        container1.pack(side=TOP)

        container2=Frame(self)
        container2.pack()

        photoContainer=Frame(self)
        photoContainer.pack()

        #Go back Button

        goBack=Button(backCon,text="Go Back",width=20,font=11,command=self.goBack)
        goBack.pack(side=LEFT,pady=10)

        #photo path button

        photoPath=Button(container2,text="Photo Path",width=30,font=11,command=self.open_image)
        photoPath.pack(side=BOTTOM)

        self.photoCanvas=Canvas(container2,width=300,height=200)
        self.photoCanvas.pack(side=TOP)

        #Add photo to album

        addPhotoButton=Button(self,text="Add Photo",font=11,command=self.add_Image)
        addPhotoButton.pack(side=RIGHT)

def main():
    photoPopUp=Tk()

    screenWidth = photoPopUp.winfo_screenwidth()
    screenHeight = photoPopUp.winfo_screenheight()

    appWidth = 600
    appHeight = 600

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)

    photoPopUp.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    user_addPhoto_page = addPhotoPopUp(master=photoPopUp)
    user_addPhoto_page.pack(expand=True, fill="both")
    photoPopUp.mainloop()

