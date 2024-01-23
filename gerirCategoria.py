import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ManageCategoriesPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.tree = ttk.Treeview(self, selectmode="browse", columns=("Category"), show="headings", height=15)
        self.tree.heading('Category', text='Categories')
        self.tree.column('Category', anchor='center', width=200)
        self.tree.grid(row=0, column=0, padx=10, pady=10,rowspan=5, columnspan=2)
        style = ttk.Style()
        style.configure("Treeview", highlightthickness=0, font=('Calibri', 12)) 
        style.configure("Treeview.Heading", font=('Comic Sans MS', 11))
        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 
        self.load_category("files\\categories.txt")
        self.delete_button = tk.Button(self, text='Delete Category',font=11,command=self.deleteSelected)
        self.delete_button.grid(row=1, column=2, padx=10,pady=10)
        self.delete_button = tk.Button(self, text='Add Category',font=11,command=self.Add_Category)
        self.delete_button.grid(row=1, column=3, pady=10)
        self.category_label=tk.Label(self,text="New Category:",font=11)
        self.category_label.grid(row=0,column=2)
        self.category_entry=tk.Entry(self,width=25,font=11)
        self.category_entry.grid(row=0,column=3) 

    def load_category(self,file_path):
         f=open(file_path, 'r', encoding='utf-8')
         for line in f:
             content = line.strip().split(';')
             self.tree.insert('', 'end', values=(content[0]))

    def Add_Category(self):
        Category =self.category_entry.get()
        f = open("files\\categories.txt", "r", encoding="utf-8")
        lines = f.readlines()
        f.close()
    
        for line in lines:
            content = line.split(";")
            if (content[0] == Category):
                messagebox.showerror(title="Category", message="That category already exists.")
                return
    
        newLine = Category +";"+ "\n"
        f = open("files\\categories.txt", "a", encoding="utf-8")
        f.write(newLine)
        f.close()
        self.tree.insert('', 'end', values=Category)        
    
    def deleteSelected(self):
        selected = self.tree.selection()[0]
        currentItem = self.tree.focus()
        category = self.tree.item(currentItem, "values")[0]
        file_path = "files\\categories.txt"
        f=open(file_path, "r", encoding="utf-8")
        lines = f.readlines()
        new_lines = []
        for line in lines:
            content = line.split(";")
            if content[0] != category:
                new_lines.append(line)
        f=open(file_path, "w", encoding="utf-8")
        f.writelines(new_lines)
        self.tree.delete(selected)



def main():
    root = tk.Tk()
    root.title("Category Management System")
    root.geometry("800x600") 
    ManageCategoriesPage(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()