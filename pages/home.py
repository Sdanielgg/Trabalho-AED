#Barrinha em cima com os diversos caminhos(dashboard, home(para dar referesh), notificações, logout), na parte principal vai ter
from tkinter import *

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

def clique_do_botao():
    print("O botão foi clicado!")

window = tk.Tk()

button = tk.Button(janela, text="Clique em mim!", command=clique_do_botao)

button.pack()

home.mainloop()
