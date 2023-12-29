from tkinter import *

newAlbum=Tk()

screenWidth = newAlbum.winfo_screenwidth()
screenHeight = newAlbum.winfo_screenheight()

appWidth = 1000
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

newAlbum.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
newAlbum.mainloop()