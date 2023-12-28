#!/usr/bin/python

import sys
from tkinter import *

class App():

    def __init__(self):
        self.geometry = "600x600"

    def login(self):
        # comparar as cardenciais com as guardadas no ficheiro
        print('Hello login :-)')

    def cardentials(self):
        frame = Frame(self.window)
        frame.pack()

        Label(frame, text="Username:").grid(row=0, column=0)
        Label(frame, text="Password:").grid(row=1, column=0)

        username_entry = Entry(frame)
        password_entry = Entry(frame, show="*")

        username_entry.grid(row=0, column=1)
        password_entry.grid(row=1, column=1)

        login_button = Button(frame, text="Login", command=self.login)
        login_button.grid(row=2, column=1)

    def init(self):
        self.window = Tk()
        self.window.title("Login Page")
        self.window.geometry(self.geometry)

        self.cardentials()

        self.window.mainloop()

def main(args):
    app = App()
    app.init()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))