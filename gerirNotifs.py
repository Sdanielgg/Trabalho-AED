import tkinter as tk
from tkinter import ttk, messagebox

class NotificationManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Notification Manager")

        self.tree = ttk.Treeview(root, columns=("Notifications"), show="headings")
        self.tree.heading("Notifications", text="Notifications")
        self.tree.column("Notifications", width=350, anchor="center")
        self.tree.pack(side="left", padx=10, pady=10)
        self.tree.place(x=50, y=50)

        user_frame = tk.Frame(root)
        user_frame.pack(side="right", padx=10, pady=10)

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
    root.geometry("450x300") 
    app = NotificationManager(root)
    root.resizable(False, False)
    root.mainloop()