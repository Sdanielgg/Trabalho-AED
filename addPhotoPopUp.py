from tkinter import *

photoPopUp=Tk()

screenWidth = photoPopUp.winfo_screenwidth()
screenHeight = photoPopUp.winfo_screenheight()

appWidth = 600
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

photoPopUp.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")


#photo path button
photoPath=Button(photoPopUp,text="Photo Path",width=30)
photoPath.place(x=0,y=0)

#photo description (only a few char)

descriptionLabel=Label(photoPopUp,text="Description",font=11)
descriptionLabel.place(x=30,y=0)

description=Text(photoPopUp,height=5,width=40,font=11)
description.place(x=30,y=30)

addPhotoButton=Button(photoPopUp,text="Add Photo",font=11)
 
photoPopUp.mainloop()