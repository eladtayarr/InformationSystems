# ui/inventory_alerts.py
import tkinter as tk
import sqlite3

class InventoryAlertsWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="התראות על מלאי נמוך:").pack(pady=10)
        self.alerts_list = tk.Listbox(self.frame, width=60)
        self.alerts_list.pack()

        self.load_alerts()

    def load_alerts(self):
        conn = sqlite3.connect("store_system.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT InventoryAlert.alert_id, Product.name, InventoryAlert.alert_type, InventoryAlert.alert_time
            FROM InventoryAlert
            JOIN Product ON InventoryAlert.product_id = Product.product_id
            WHERE InventoryAlert.alert_type = 'LOW_STOCK'
            ORDER BY InventoryAlert.alert_time DESC
        """)
        alerts = cursor.fetchall()
        conn.close()

        for alert in alerts:
            alert_id, name, alert_type, alert_time = alert
            self.alerts_list.insert(tk.END, f"[{alert_time}] {name} - {alert_type}")
