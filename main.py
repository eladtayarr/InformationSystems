# main.py
import tkinter as tk
from ui.login import LoginWindow


def main():
    root = tk.Tk()
    root.title("\u05de\u05e2\u05e8\u05db\u05ea \u05e0\u05d9\u05d4\u05d5\u05dc \u05dc\u05e7\u05d5\u05d7\u05d5\u05ea \u05d5\u05de\u05dc\u05d0\u05d9")
    app = LoginWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
