import tkinter as tk

import ui.widgets.periodic as periodic


class Home(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_home_tab()

    def create_home_tab(self):
        theme1 = tk.PhotoImage(file='assets/Capture.png')
        them1 = tk.Label(self.parent, image=theme1)
        them1.place(x=-50, y=-22)
        them1.image = theme1

        periodic.PeriodicTable(self.parent)
