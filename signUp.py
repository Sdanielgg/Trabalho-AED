from tkinter import *
signUp=Tk()
screenWidth = signUp.winfo_screenwidth()
screenHeight = signUp.winfo_screenheight()

appWidth = 600
appHeight = 300

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

signUp.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

signUp.title("Sign Up")
signUp.resizable(0,0)

# Username Label/Entry
lbl_username = Label(signUp, text="Username:",font=11)
lbl_username.place(x=170, y=40)

txt_username = Entry(signUp, width=25,font=11)
txt_username.place(x=270, y=40)

# Password Label/Entry
lbl_password = Label(signUp, text="Password:", fg="red", font= 11)
lbl_password.place(x=170, y=70)

txt_password = Entry(signUp, width=25,font=11, show="*")
txt_password.place(x=270, y=70)

# Password Confirm Label/Entry
lbl_passwordConfirm = Label(signUp, text="Password Confirmation:", fg="red", font= 11)
lbl_passwordConfirm.place(x=55, y=100)

txt_passwordConfirm = Entry(signUp, width=25, show="*",font=11)
txt_passwordConfirm.place(x=270, y=100)

#Buttons
btn_signUp = Button(signUp, text="Sign Up", relief="raised", bd=3, width=10, font=11)
btn_signUp.place(x=270, y=150)

btn_signIn= Button(signUp, text="Sign In", relief="raised", bd=3, width=10, font=11)
btn_signIn.place(x=400,y=150)


signUp.mainloop()