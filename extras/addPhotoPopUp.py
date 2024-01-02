from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

#Functions

def open_image():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        display_image(file_path)


def display_image(file_path):
    # Open the image
    original_image = Image.open(file_path)

    aspect_ratio = original_image.width / original_image.height
    
    target_size = (200, int(200 / aspect_ratio))
    resized_image = original_image.resize(target_size, Image.ADAPTIVE)
    
    photo = ImageTk.PhotoImage(resized_image)
    
    photoCanvas.config(width=target_size[0], height=target_size[1])
    
    photoCanvas.create_image(0, 0, anchor=NW, image=photo)
    photoCanvas.image = photo


#Window
photoPopUp=Tk()
photoPopUp.configure(bg="grey")

screenWidth = photoPopUp.winfo_screenwidth()
screenHeight = photoPopUp.winfo_screenheight()

appWidth = 600
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

photoPopUp.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

#Containers
backCon=Frame(photoPopUp,bg="grey")
backCon.pack(side=TOP)
container1=Frame(photoPopUp,bg="grey")
container1.pack(side=TOP)

container2=Frame(photoPopUp,bg="grey")
container2.pack()

photoContainer=Frame(photoPopUp)
photoContainer.pack()


#Go back Button

goBack=Button(backCon,text="Go Back",width=20,font=11)
goBack.pack(side=LEFT)

#photo path button

photoPath=Button(container2,text="Photo Path",width=30,font=11,command=open_image)
photoPath.pack(side=TOP)

photoCanvas=Canvas(container2,bg="grey",width=200,height=200)
photoCanvas.pack(side=TOP)

#photo description (only a few char)

descriptionLabel=Label(container2,text="Description",font=11,bg="grey")
descriptionLabel.pack(side=TOP)

description=Text(container2,height=5,width=40,border=10,font=11)
description.pack(side=BOTTOM)

#Add photo to album

addPhotoButton=Button(photoPopUp,text="Add Photo",font=11)
addPhotoButton.pack(side=RIGHT)
 
photoPopUp.mainloop()