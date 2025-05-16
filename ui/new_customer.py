# ui/new_customer.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

class NewCustomerWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="שם פרטי:").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(self.frame)
        self.first_name_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="שם משפחה:").grid(row=1, column=0)
        self.last_name_entry = tk.Entry(self.frame)
        self.last_name_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="אימייל:").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="טלפון:").grid(row=3, column=0)
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.grid(row=3, column=1)

        tk.Button(self.frame, text="שמור לקוח", command=self.save_customer).grid(row=4, column=0, columnspan=2, pady=10)

    def save_customer(self):
        first = self.first_name_entry.get()
        last = self.last_name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not first or not last:
            messagebox.showwarning("שגיאה", "יש למלא לפחות שם פרטי ושם משפחה")
            return

        customer_id = f"CUST{first[:2].upper()}{last[:2].upper()}"

        conn = sqlite3.connect("store_system.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Customer (customer_id, first_name, last_name, email, phone) VALUES (?, ?, ?, ?, ?)",
                           (customer_id, first, last, email, phone))
            conn.commit()
            messagebox.showinfo("הצלחה", "הלקוח נשמר בהצלחה!")
            self.frame.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("שגיאה", "לקוח עם מזהה זה כבר קיים.")
        finally:
            conn.close()
