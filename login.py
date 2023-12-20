#!python

from tkinter import *

# Create the main window
Window = Tk()
Window.title("Login Page")
Window.geometry("800x600")

frame = Frame(Window)
frame.pack()

Label(frame, text="Username:", font=14).grid(row=0, column=0)
Label(frame, text="Password:", font=14).grid(row=1, column=0)

username_entry = Entry(frame, width=20, font=14)
password_entry = Entry(frame, width=20, font=14, show="*")

username_entry.grid(row=0, column=1, columnspan=2, pady=10)
password_entry.grid(row=1, column=1, columnspan=2, pady=10)

login_button = Button(frame, width=10, text="Login", font=10)
login_button.grid(row=2, column=1)

signup_button = Button(frame, width=10, text="Sign Up", font=10)
signup_button.grid(row=2, column=2)


Window.mainloop()