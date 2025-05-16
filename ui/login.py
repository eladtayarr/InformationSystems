# ui/login.py
import tkinter as tk
from tkinter import messagebox
import sqlite3
from ui.main_menu import MainMenu

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="שם משתמש:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="סיסמה:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.frame, text="התחבר", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect("store_system.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SystemUser WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("הצלחה", f"ברוך הבא, {username}!")
            self.frame.destroy()
            MainMenu(self.master, username)
        else:
            messagebox.showerror("שגיאה", "שם משתמש או סיסמה שגויים.")
