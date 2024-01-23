from tkinter import *
class AdminHome(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    def create_widgets(self):
        self.gerirCategorias=Button(self,text="Categories",width=20,font=11,command=self.openCategories)
        self.gerirCategorias.place(x=100,y=100)
        self.gerirUtilizadores=Button(self,text="Users",width=20,font=11,command=self.openUsers)
        self.gerirUtilizadores.place(x=100,y=200)
    def openCategories(self):
        self.master.destroy()
        import gerirCategoria
        gerirCategoria.main()
    def openUsers(self):
        self.master.destroy()
        import gerirUtilizadores
        gerirUtilizadores.main()
def main():
    adminHome=Tk()
    screenWidth = adminHome.winfo_screenwidth()
    screenHeight = adminHome.winfo_screenheight()

    appWidth = 600
    appHeight = 600

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)

    adminHome.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
    adminHome.title("adminHome")
    adminHome.resizable(0,0)
    user_signIn_page = AdminHome(master=adminHome)
    user_signIn_page.pack(expand=True, fill="both")

    adminHome.mainloop() 
