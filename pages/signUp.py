from tkinter import *
from tkinter import messagebox
import tkinter as tk

#functions

class SignUp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def newUser(self):
        Username =self.txt_username.get()
        Password =self.txt_password.get()
        PasswordConfirm=self.txt_passwordConfirm.get()
        if (len(Password)<8):
            messagebox.showerror(title="Not enough characters.",message="Your Password needs to have at least 8 characters.")

        f_users = open("files\\users.txt", "r", encoding="utf-8")
        lines = f_users.readlines()
        f_users.close()

        for line in lines:
            content = line.split(";")
            if (content[0] == Username):
                messagebox.showerror(title="Sign up", message="That username is already in use.")
                return
            if (Password!=PasswordConfirm):
                messagebox.showerror(title="Password error",message="Password doesn't match.")
                return
        
        newLine = Username + ";" + Password + ";" + "User"+";"+ "loggedOut"+";"+"\n"
        f_users = open("files\\users.txt", "a", encoding="utf-8")
        f_users.write(newLine)
        f_users.close()
    def signInOpen(self):
        self.master.destroy()
        import signIn

    def create_widgets(self):

        #Username Label/Entry
        
        lbl_username = Label(self, text="Username:",font=11)
        lbl_username.place(x=110, y=40)

        self.txt_username = Entry(self, width=25,font=11)
        self.txt_username.place(x=210, y=40)

        # Password Label/Entry

        lbl_password = Label(self, text="Password:", fg="red", font= 11)
        lbl_password.place(x=110, y=70)

        self.txt_password = Entry(self, width=25,font=11, show="*")
        self.txt_password.place(x=210, y=70)

        # Password Confirm Label/Entry

        lbl_passwordConfirm = Label(self, text="Confirm Password:", fg="red", font= 11)
        lbl_passwordConfirm.place(x=37, y=100)

        self.txt_passwordConfirm = Entry(self, width=25, show="*",font=11)
        self.txt_passwordConfirm.place(x=210, y=100)

        #Buttons

        btn_signUp = Button(self, text="Sign Up", relief="raised", bd=3, width=10, font=11,command=self.newUser)
        btn_signUp.place(x=210, y=150)

        btn_signIn= Button(self, text="Sign In", relief="raised", bd=3, width=10, font=11,command=self.signInOpen)
        btn_signIn.place(x=340,y=150)

#window        
def main():
    signUp = Tk()
    signUp.configure(bg="#D9D9D9")
    signUp.title("Sign Up")
    signUp.resizable(0,0)
    appWidth = 600
    appHeight = 300 
    screenWidth = signUp.winfo_screenwidth()
    screenHeight = signUp.winfo_screenheight()
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    signUp.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    user_signUp_page = SignUp(master=signUp)
    user_signUp_page.pack(expand=True, fill="both")

    signUp.mainloop()


if __name__ == "__main__":
    main()
    
