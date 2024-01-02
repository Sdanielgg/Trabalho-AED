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

        menu = Menu(self.window)
        self.window.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Novo Album")
        fileMenu.add_command(label="Importar Album")
        fileMenu.add_command(label="Exportar Album")
        fileMenu.add_command(label="Sair", command=self.window.quit)
        menu.add_cascade(label="Ficheiro", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Desfazer")
        editMenu.add_command(label="Refazer")
        menu.add_cascade(label="Editar", menu=editMenu)

        adminMenu = Menu(menu)
        adminMenu.add_command(label="Gerir Utilizadores")
        adminMenu.add_command(label="Gerir Categorias")
        adminMenu.add_command(label="Configurar Notificações")
        menu.add_cascade(label="Administração", menu=adminMenu)

        albumsMenu = Menu(menu)
        albumsMenu.add_command(label="Gerir")
        albumsMenu.add_command(label="Listar")
        menu.add_cascade(label="Albuns", menu=albumsMenu)


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
            self.home()

        login_button = Button(frame, text="Login", command=login)
        login_button.grid(row=2, column=1)

    def init(self):
        self.window = Tk()
        self.window.title("Login Page")
        self.window.geometry(self.geometry)

        bg = PhotoImage(file = "./images/background.png")
        label = Label(self.window, image = bg) 
        label.place(x = 0, y = 0) 

        self.cardentials()

        self.window.mainloop()

def main(args):
    app = App()
    app.init()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))