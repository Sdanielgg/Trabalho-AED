import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("1024x768")
window.title("User")


class User:
    def __init__(self, main):

        frame = ttk.Frame(window, borderwidth=200, relief="solid")
        frame.place(x=10, y=260, width=1420, height=625)

        name = tk.Label(window, text="User", font=('Arial', 35))
        name.place(x=250, y=130)

        stats = tk.Label(window, text="Statistics", font=('Arial', 20))
        stats.place(x=40, y=310)

        views = tk.Label(window, text="Views:", font=('Arial', 20))
        views.place(x=50, y=390)

        content = tk.Label(window, text="Content made:", font=('Arial', 20))
        content.place(x=50, y=460)

        comments = tk.Label(window, text="Number of comments:", font=('Arial', 20))
        comments.place(x=50, y=530)

        chooseContent = tk.Label(window, text="Content by category:", font=('Arial', 20))
        chooseContent.place(x=1000, y=310)

        style = ttk.Style()
        style.configure("TCombobox", padding=5, relief="flat", background="#ececec")
        category_list = ['Sports', 'Crafts', 'Nature']
        categories = ttk.Combobox(window, values=category_list, state='readonly', font=('Arial', 17), style="TCombobox")
        categories.set("Select a category")
        categories.place(x=1000, y=350)

        pp = tk.Label(window, image = "")
        pp.place(x=10, y=10)

yes = User(window)


window.mainloop()