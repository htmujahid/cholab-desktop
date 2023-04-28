import platform
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import ui.window as window

import ui.screens.home as home

class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.parent.geometry('850x600+120+80')
        self.parent.minsize(850,600)
        self.parent.maxsize(850,600)
        self.parent.title("Cholab")

    def init_ui(self):
        self.window = window.Window(self.parent)
        

def main():
    print("Cholab launched!")
    print(("OS:%s") % (platform.system()))
    root = tk.Tk()
    app = Main(root)
    app.init_ui()
    root.mainloop()

if __name__ == '__main__':
    main()