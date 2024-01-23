from tkinter import *
class ManageCategoriesPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
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

    home.mainloop() 