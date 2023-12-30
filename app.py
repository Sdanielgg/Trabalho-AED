#!python

import sys
from tkinter import *
from tkinter import messagebox
import re

class App():

    def __init__(self):
        self.geometry = "600x600"
        self.accounts = {
            "test@example.com": {
                "name": "Teste da Silva",
                "user": "admin",
                "password": "123456789",
                "online": False
            },
            "petunia@example.com": {
                "name": "Petúnia Dias",
                "user": "user",
                "password": "987654321",
                "online": False
            }
        }


    def valid_login(self, username, password):
        if username in self.accounts and self.accounts[username]["password"] == password:
            return True

        return False


    def test_cardentials(self, username, password):

        if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
            return "Email incorrecto!"
        
        if len(password) < 8:
            return "Password incorrecta!"

        if not self.valid_login(username, password):
            return "Password ou login incorrecto!"
        
        return ""

    def home(self):
        left_frame = Frame(self.window, width=200, height=400)
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        tool_bar = Frame(left_frame, width=180, height=185, bg="green")
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        Label(left_frame, text="MyFotos").grid(row=1, column=0, padx=5, pady=5)


    def cardentials(self):
        frame = Frame(self.window)
        frame.pack()

        Label(frame, text="Username:").grid(row=0, column=0)
        Label(frame, text="Password:").grid(row=1, column=0)

        username_entry = Entry(frame)
        password_entry = Entry(frame, show="*")

        username_entry.grid(row=0, column=1)
        password_entry.grid(row=1, column=1)

        def login():
            username = username_entry.get()
            password = password_entry.get()

            error = self.test_cardentials(username, password)
            if error != "":
                messagebox.showerror("Erro", error)
                return
            
            frame.destroy()
            self.home();

        login_button = Button(frame, text="Login", command=login)
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