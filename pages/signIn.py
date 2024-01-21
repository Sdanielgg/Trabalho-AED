from tkinter import *
from tkinter import messagebox
signIn=Tk()

#funções
def logIn():
    username=txt_username.get()
    password=txt_password.get()

    f_users = open("files\\users.txt", "r", encoding="utf-8")
    lines = f_users.readlines()
    f_users.close()

    for i, line in enumerate(lines):
        content = line.split(";")
        if content[0] == username and content[1] == password:
            print("Login successful!")
            # Update the status in the file or do any other required operation
            content[3] = "Logged"
            lines[i] = ";".join(content)

            f_users = open("files\\users.txt", "w", encoding="utf-8")
            f_users.writelines(lines)

        else:
             messagebox.showerror(title="Wrong Credentials", message="Either your username or your password doesn't match up.")



#window
screenWidth = signIn.winfo_screenwidth()
screenHeight = signIn.winfo_screenheight()

appWidth = 600
appHeight = 300

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

signIn.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

signIn.title("Sign In")
signIn.resizable(0,0)

# Username Label/Entry
lbl_username = Label(signIn, text="Username:",font=11)
lbl_username.place(x=110, y=40)

txt_username = Entry(signIn, width=25,font=11)
txt_username.place(x=210, y=40)

#Password Label/Entry 
lbl_password = Label(signIn, text="Password:", fg="red", font= 11)
lbl_password.place(x=110, y=70)

txt_password = Entry(signIn, width=25,font=11, show="*")
txt_password.place(x=210, y=70)

# Buttons
btn_signUp = Button(signIn, text="Sign Up", relief="raised", bd=3, width=10, font=11)
btn_signUp.place(x=210, y=115)

btn_signIn= Button(signIn, text="Sign In", relief="raised", bd=3, width=10, font=11,command=logIn)
btn_signIn.place(x=340,y=115)


signIn.mainloop()