from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

#Functions
class addPhotoPopUp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def open_image(self):
        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.display_image(file_path)


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
        backCon=Frame(self.photoPopUp,bg="grey")
        backCon.pack(side=TOP)
        container1=Frame(self.photoPopUp,bg="grey")
        container1.pack(side=TOP)

        container2=Frame(self.photoPopUp,bg="grey")
        container2.pack()

        photoContainer=Frame(self.photoPopUp)
        photoContainer.pack()


        #Go back Button

        goBack=Button(backCon,text="Go Back",width=20,font=11)
        goBack.pack(side=LEFT,pady=10)

        #photo path button

        photoPath=Button(container2,text="Photo Path",width=30,font=11,command=self.open_image)
        photoPath.pack(side=BOTTOM)

        photoCanvas=Canvas(container2,bg="grey",width=300,height=200)
        photoCanvas.pack(side=TOP)

        #photo description (only a few char)


        #Add photo to album

        addPhotoButton=Button(self.photoPopUp,text="Add Photo",font=11)
        addPhotoButton.pack(side=RIGHT)

def main():
    photoPopUp=Tk()
    photoPopUp.configure(bg="grey")

    screenWidth = photoPopUp.winfo_screenwidth()
    screenHeight = photoPopUp.winfo_screenheight()

    appWidth = 600
    appHeight = 600

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)

    photoPopUp.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
main()