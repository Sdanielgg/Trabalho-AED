import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ManageUsersPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        
    def load_users(self):
         f_users=open('files\\users.txt', 'r', encoding='utf-8')
         for line in f_users:
             content = line.strip().split(';')
             self.tree.insert('', 'end', values=(content[0],content[1]))
    
    def deleteSelected(self):
        selected = self.tree.selection()[0]
        currentItem = self.tree.focus()
        username = self.tree.item(currentItem, "values")[0]
        file_path = "files\\users.txt"
        f_users=open(file_path, "r", encoding="utf-8")
        lines = f_users.readlines()
        new_lines = []
        for line in lines:
            content = line.split(";")
            if content[0] != username:
                new_lines.append(line)
        f_users=open(file_path, "w", encoding="utf-8")
        f_users.writelines(new_lines)
        self.tree.delete(selected)

    def create_widgets(self):
        self.tree = ttk.Treeview(self, selectmode="browse", columns=("Name","User Type"), show="headings", height=20)
        self.tree.heading('Name', text='User Name')
        self.tree.heading('User Type', text='User Type')
        self.tree.column('Name', anchor='center', width=200)
        self.tree.column('User Type', anchor='center', width=150)
        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, background="#54494F" ,bd=0, font=('Calibri', 11)) 
        style.configure("Treeview.Heading" ,font=('Comic Sans MS', 11))
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 
        self.load_users()
        self.delete_button = tk.Button(self, text='Delete User',command=self.deleteSelected)
        self.delete_button.grid(row=1, column=0, pady=10)

def main():
    root = tk.Tk()
    root.title("User Management System")
    root.geometry("800x600") 
    ManageUsersPage(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()