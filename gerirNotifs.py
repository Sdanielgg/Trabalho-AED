import tkinter as tk
from tkinter import ttk, messagebox

class NotificationManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Notification Manager")

        self.users = ["User1", "User2", "User3"]

        self.tree = ttk.Treeview(root, columns=("User", "Notification"), show="headings")
        self.tree.heading("User", text="User")
        self.tree.heading("Notification", text="Notification")
        self.tree.pack(side="left", padx=10, pady=10)

        user_frame = tk.Frame(root)
        user_frame.pack(side="right", padx=10, pady=10)

        self.selected_user = tk.StringVar()
        self.selected_user.set(self.users[0])
        user_menu = tk.OptionMenu(user_frame, self.selected_user, *self.users)
        user_menu.pack(pady=5)

        self.notification_entry = tk.Entry(user_frame, width=40)
        self.notification_entry.pack(pady=5)

        notify_button = tk.Button(user_frame, text="Notify", command=self.notify_user)
        notify_button.pack(pady=5)

        add_album_button = tk.Button(user_frame, text="Add Album")
        add_album_button.pack(pady=55)

    def notify_user(self):
        user = self.selected_user.get()
        notification_text = self.notification_entry.get()

        if user and notification_text:
            self.tree.insert("", "end", values=(user, notification_text))
            messagebox.showinfo(f"Notification for {user}", f"Notification: {notification_text}")
        else:
            messagebox.showwarning("Incomplete Information", "Please select a user and enter a notification text.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600") 
    app = NotificationManager(root)
    root.mainloop()