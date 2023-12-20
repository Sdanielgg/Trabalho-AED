from tkinter import *
# Create the main window
Window =Tk()
Window.title("Login Page")
Window.geometry("600x600")

frame = Frame(Window)
frame.pack()

Label(frame, text="Username:").grid(row=0, column=0)
Label(frame, text="Password:").grid(row=1, column=0)

username_entry = Entry(frame)
password_entry = Entry(frame, show="*")

username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

login_button = Button(frame, text="Login")
login_button.grid(row=2, column=1)

Window.mainloop()