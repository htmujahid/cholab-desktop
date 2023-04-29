import os
import tkinter as tk
from PIL import Image, ImageTk

import ui.widgets.periodic as periodic


class Home(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_home_tab()

    def create_home_tab(self):
        image_path = Image.open(os.path.join('assets', 'Capture.png'))
        theme1 = ImageTk.PhotoImage(image_path)
        them1 = tk.Label(self.parent, image=theme1)
        them1.place(x=-50, y=-22)
        them1.image = theme1

        periodic.PeriodicTable(self.parent)
