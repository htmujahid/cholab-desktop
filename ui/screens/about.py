import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


class About(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_about_tab()

    def create_about_tab(self):
        self.parent.configure(background='white')
        style = ttk.Style(self.parent)
        style.configure('TLabel', background='white', foreground='black')
        heading1 = ttk.Label(self.parent, text='Abstract', font=('Arial', 15), foreground='black', background='white')
        heading1.grid(row=0, sticky='w')
        label1 = ttk.Label(self.parent, text=(
            'The main purpose of making this app is to provide all the properties of an element at a single offline platform which is not observed before it. This is the best ever created open source GUI application which deals almost all the things which are related to Chemical Elements. In this application you have multiple option to see the properties of an element. You can see properties by only clicking the element in periodic table, you can simply search by atomic number, symbol or element name. You can view a property of every element in periodic table by simply clicking on the button. In short it is such an app which handle all issues regarding C.E properties.'),
            wraplength=700)
        label1.grid(row=5, sticky='w')
        heading1 = ttk.Label(self.parent, text='Developers', font=('Arial', 15))
        heading1.grid(row=20, sticky='w')
        labelt = ttk.Label(self.parent, text='i.   Talha Mujahid')
        labelt.grid(row=21, sticky='w')
        labelu = ttk.Label(self.parent, text='ii.   Muhammad Uzaier')
        labelu.grid(row=22, sticky='w')
        labela = ttk.Label(self.parent, text='iii.   Altaf Ahmad')
        labela.grid(row=23, sticky='w')
