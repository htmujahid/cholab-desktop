import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


class About(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_about_tab()

    def create_about_tab(self):
        heading1 = tk.Label(self.parent, text='Abstract', font=('Arial', 15))
        heading1.grid(row=0, sticky='w')
        label1 = tk.Label(self.parent, text=(
            'The main purpose of making this app is to provide all the properties of an element at a single offline platform which is not observed.'))
        label1.grid(row=1, sticky='w')
        label1 = tk.Label(self.parent, text=(
            'before it. This is the best ever created open source GUI application which deals almost all the things which are related to Chemical '))
        label1.grid(row=2, sticky='w')
        label1 = tk.Label(self.parent, text=(
            'Elements. In this application you have multiple option to see the properties of an element. You can see properties by only clicking '))
        label1.grid(row=3, sticky='w')
        label1 = tk.Label(self.parent, text=(
            'the element in periodic table, you can simply search by atomic number, symbol or element name. You can view a property of every '))
        label1.grid(row=4, sticky='w')
        label1 = tk.Label(self.parent, text=(
            'element in periodic table by simply clicking on the button. In short it is such an app which handle all issues regarding C.E properties.'))
        label1.grid(row=5, sticky='w')
        heading1 = tk.Label(self.parent, text='Developers', font=('Arial', 15))
        heading1.grid(row=20, sticky='w')
        labelt = tk.Label(self.parent, text='i.   Talha Mujahid')
        labelt.grid(row=21, sticky='w')
        labelu = tk.Label(self.parent, text='ii.   Muhammad Uzaier')
        labelu.grid(row=22, sticky='w')
        labela = tk.Label(self.parent, text='iii.   Altaf Ahmad')
        labela.grid(row=23, sticky='w')
