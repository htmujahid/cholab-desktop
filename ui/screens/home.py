import os
import tkinter as tk
from tkinter import ttk

import ui.widgets.periodic as periodic


class Home(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_home_tab()

    def create_home_tab(self):
        self.parent.configure(background='white')
        periodic.PeriodicTable(self.parent)
