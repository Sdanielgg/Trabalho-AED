from tkinter import *
signIn=Tk()

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
btn_signIn = Button(signIn, text="Sign Up", relief="raised", bd=3, width=10, font=11)
btn_signIn.place(x=210, y=115)

btn_signIn= Button(signIn, text="Sign In", relief="raised", bd=3, width=10, font=11)
btn_signIn.place(x=340,y=115)


signIn.mainloop()