from tkinter import *
from tkinter import messagebox

class SignIn(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.eyeIconHidden = PhotoImage(file="images\\eyeIconShow.png")
        self.eyeIconNotHidden = PhotoImage(file="images\\eyeIconHide.png")
        self.create_widgets()

    def goToHome(self):
        self.master.destroy()
        import home
    def goToSignUp(self):
        import signUp
        
    def logIn(self):
        username = self.txt_username.get()
        password = self.txt_password.get()

        f_users = open("files\\users.txt", "r", encoding="utf-8")
        lines = f_users.readlines()
        f_users.close()

        for i, line in enumerate(lines):
            content = line.split(";")
            if (content[0] == username and content[1] == password):
                content[3] = "Logged"
                lines[i] = ";".join(content)
                
                f_users = open("files\\users.txt", "w", encoding="utf-8")
                f_users.writelines(lines)
                self.goToHome()
                return
            
            messagebox.showerror(title="Wrong Credentials", message="Either your username or your password doesn't match up.")
            return

    def toggle_password_visibility(self):
        current_state = self.txt_password.cget("show")
        if current_state == "*":
            new_state = ""
            self.txt_password.config(show=new_state)
            self.showPasswordIcon.config(image=self.eyeIconNotHidden)
        else:
            new_state = "*"
            self.txt_password.config(show=new_state)
            self.showPasswordIcon.config(image=self.eyeIconHidden)

    def create_widgets(self):
        # Username Label/Entry
        lbl_username = Label(self, text="Username:", font=11)
        lbl_username.place(x=110, y=40)

        self.txt_username = Entry(self, width=25, font=11)
        self.txt_username.place(x=210, y=40)

        # Password Label/Entry
        lbl_password = Label(self, text="Password:", fg="red", font=11)
        lbl_password.place(x=110, y=70)

        self.txt_password = Entry(self, width=25, font=11, show="*")
        self.txt_password.place(x=210, y=70)

        self.showPasswordIcon = Button(self, image=self.eyeIconHidden, width=20, height=20, command=self.toggle_password_visibility)
        self.showPasswordIcon.place(x=500, y=70)

        # Buttons
        btn_signUp = Button(self, text="Sign Up", relief="raised", bd=3, width=10, font=11,command=self.goToSignUp)
        btn_signUp.place(x=340, y=115)

        btn_signIn = Button(self, text="Sign In", relief="raised", bd=3, width=10, font=11, command=self.logIn)
        btn_signIn.place(x=210, y=115)

def main():
    signIn = Tk()
    signIn.configure(bg="#D9D9D9")
    signIn.title("Sign In")
    signIn.resizable(0, 0)
    appWidth = 600
    appHeight = 300
    screenWidth = signIn.winfo_screenwidth()
    screenHeight = signIn.winfo_screenheight()
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    signIn.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")
    user_signIn_page = SignIn(master=signIn)
    user_signIn_page.pack(expand=True, fill="both")

    signIn.mainloop()

if __name__ == "__main__":
    main()
