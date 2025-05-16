# ui/login.py
import tkinter as tk
from tkinter import messagebox
import sqlite3
from ui.main_menu import MainMenu

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="#5A60EA")
        self.frame = tk.Frame(master, bg="white", padx=30, pady=30)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        master.title("התחברות למערכת ניהול חנות") 
        master.geometry("800x1000")

        tk.Label(self.frame, text="התחברות", font=("Helvetica", 16, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 20))

        tk.Label(self.frame, text="שם משתמש", bg="white").grid(row=1, column=0, sticky="w")
        self.username_entry = tk.Entry(self.frame, width=30)
        self.username_entry.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        tk.Label(self.frame, text="סיסמה", bg="white",justify="right", anchor="ne").grid(row=3, column=0, sticky="w")
        self.password_entry = tk.Entry(self.frame, show="*", width=30)
        self.password_entry.grid(row=4, column=0, columnspan=2, pady=(0, 10))

        tk.Button(self.frame, text="התחבר", bg="#2D9CDB", fg="white", width=25, command=self.login).grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="שחכת סיסמה?",justify="right", anchor="e",fg="gray", bg="white").grid(row=5, column=0, sticky="w")
        tk.Label(self.frame, text="לא רשום?", bg="white").grid(row=7, column=0, sticky="w")
        tk.Label(self.frame, text="הרשמה למערכת", fg="blue", bg="white", cursor="hand2").grid(row=7, column=1, sticky="e")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect("store_system.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SystemUser WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            self.frame.destroy()
            MainMenu(self.master, username)
        else:
            messagebox.showerror("Error", "Invalid username or password.")