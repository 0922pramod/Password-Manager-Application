#type: ignore
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import hashlib
import getpass

college_passwords={
    "student_portal": {"username": "rohit", "password":hashlib.sha256("hitman@45".encode())},
    "library": {"username":"kohli","password":hashlib.sha256("virat@18".encode())},
    "email_portal":{"username":"dhoni", "password":hashlib.sha256("mahi@07".encode())}
}

class Passwordmanager:
    def __init__(self, root):
        self.root=root
       # self.college_passwords=college_passwords
        self.root.title("PASSWORD MANAGER APPLICATION")
        tk.Label(root, text="PASSWORD MANAGER APPLICATION", font=("Helvetica", 16)).pack(pady=10)
        options=["Add password","Delete password","update password","list passwords","Search password", "Exit"]
        self.choice =tk.StringVar(value=options[0])
        tk.OptionMenu(root, self.choice, *options).pack(pady=5)
        tk.Button(root, text="Submit", command=self.handle_choice).pack(pady=5)

    def handle_choice(self):
        choice=self.choice.get()
        if choice=="Add password":
            self.add_password()
        elif choice=="Delete password":
            self.delete_password()
        elif choice=="update password":
            self.update_password()
        elif choice=="list password":
            self.list_passwords()
        elif choice=="search password":
            self.search_password()
        elif choice=="Exit":
            self.root.quit()

    def add_password(self):
        portal=tk.simpledialog.askstring("input","enter the portal name>>")
        username=tk.simpledialog.askstring("input","enter the  username>>")
        password=tk.simpledialog.askstring("input","enter the password>>", show='*')
        college_passwords[portal]={"username":username, "password":hashlib.sha256(password.encode())}
        messagebox.showinfo("success","password added successfully!!")
    
    def delete_password(self):
        portal=tk.simpledialog.askstring("input","enter the portal name to delete>>")
        if portal in college_passwords:
            del college_passwords[portal]
            messagebox.showinfo("success","password deleted successfully!!")
        else:
            messagebox.showerror("error", "portal not found!")
    
    def update_password(self):
        portal=tk.simpledialog.askstring("input","enter the portal name to update>>")
        if portal in college_passwords:
            password=tk.simpledialog.askstring("input","enter the new password>>", show='*')
            college_passwords[portal]["password"]=hashlib.sha256(password.encode())
            messagebox.showinfo("success","password updated successfully!!")
        else:
            messagebox.showerror("error", "portal not found!")

    def list_passwords(self):
        details=" \n ".join([f"portal: {portal}, username: {details['username']}" for portal, details in college_passwords.items()])
        messagebox.showinfo("stored passwords",details)

    def search_password(self):
        portal=tk.simpledialog.askstring("input","enter the portal name to search>>")
        if portal in college_passwords:
            details=college_passwords[portal]
            messagebox.showinfo("details", f"username:{details['username']} \n password:*********")
        else:
            messagebox.showerror("error", "portal not found!")
if __name__ =="__main__":
    root=tk.Tk()
    app=Passwordmanager(root)
    root.mainloop()