import tkinter as tk
from tkinter import ttk

dashboard = tk.Tk()
dashboard.geometry("1024x768")
dashboard.title("User")

screenWidth = dashboard.winfo_screenwidth()
screenHeight = dashboard.winfo_screenheight()

appWidth = 1000
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

dashboard.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
dashboard.resizable(0,0)

class User:
    def __init__(self, main):

        frame = ttk.Frame(dashboard, borderwidth=200, relief="solid")
        frame.place(x=10, y=260, width=1420, height=625)

        name = tk.Label(dashboard, text="User", font=('Arial', 35))
        name.place(x=250, y=130)

        stats = tk.Label(dashboard, text="Statistics", font=('Calibri', 11))
        stats.place(x=40, y=310)

        views = tk.Label(dashboard, text="Views:", font=('Calibri', 11))
        views.place(x=50, y=390)

        content = tk.Label(dashboard, text="Content made:", font=('Calibri', 11))
        content.place(x=50, y=460)

        comments = tk.Label(dashboard, text="Number of comments:", font=('Calibri', 11))
        comments.place(x=50, y=530)

        chooseContent = tk.Label(dashboard, text="Content by category:$/n".format(), font=('Calibri', 11))
        chooseContent.place(x=500, y=310)

        style = ttk.Style()
        style.configure("TCombobox", padding=5, relief="flat", background="#ececec")
        category_list = ['Sports', 'Crafts', 'Nature']
        categories = ttk.Combobox(dashboard, values=category_list, state='readonly', font=('Calibri', 11), style="TCombobox")
        categories.set("Select a category")
        categories.place(x=500, y=350)

        pp = tk.Label(dashboard, image = "")
        pp.place(x=10, y=10)

yes = User(dashboard)


dashboard.mainloop()