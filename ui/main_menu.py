# ui/main_menu.py
import tkinter as tk
from ui.new_customer import NewCustomerWindow
from ui.inventory_alerts import InventoryAlertsWindow

class MainMenu:
    def __init__(self, master, username):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text=f"שלום {username}, בחר פעולה:").pack(pady=10)

        tk.Button(self.frame, text="פתיחת תיק לקוח", width=30, command=self.open_new_customer).pack(pady=5)
        tk.Button(self.frame, text="צפייה בהתראות מלאי", width=30, command=self.view_inventory_alerts).pack(pady=5)
        tk.Button(self.frame, text="יציאה", width=30, command=master.quit).pack(pady=20)

    def open_new_customer(self):
        self.frame.destroy()
        NewCustomerWindow(self.master)

    def view_inventory_alerts(self):
        self.frame.destroy()
        InventoryAlertsWindow(self.master)
