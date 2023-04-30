import os
import tkinter as tk
from tkinter import ttk


import utils.search as search


class Search(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.search = search.Search(self.parent)
        self.search_atomic_number = self.search.search_atomic_number
        self.search_symbol = self.search.search_symbol
        self.search_name = self.search.search_name

        self.create_search_tab()

    def create_search_tab(self):
        self.parent.configure(background='white')

        style = ttk.Style()
        style.configure('TRadiobutton', background='white', foreground='black')
        style.configure('TEntry', background='white', foreground='black')
        style.configure('TButton', background='#ccc', foreground='black')

        num = tk.IntVar()

        self.namev = tk.StringVar()
        self.symbolv = tk.StringVar()
        self.atomicv = tk.StringVar()

        atomic = ttk.Radiobutton(
            self.parent, text='Atomic Number ', variable=num, value=0, command=self.atm_fun)
        symbol = ttk.Radiobutton(
            self.parent, text='Symbol                ', variable=num, value=1, command=self.sym_fun)
        name = ttk.Radiobutton(self.parent, text='Name                   ',
                               variable=num, value=2, command=self.nam_fun)

        self.labelatm = ttk.Entry(self.parent, textvariable=self.atomicv)
        self.labelsym = ttk.Entry(self.parent, textvariable=self.symbolv)
        self.labelnam = ttk.Entry(self.parent, textvariable=self.namev)

        self.btnatm = ttk.Button(
            self.parent, text='Search', command=lambda: self.search_atomic_number(self.atomicv.get()))
        self.btnsym = ttk.Button(
            self.parent, text='Search', command=lambda: self.search_symbol(self.symbolv.get()))
        self.btnnam = ttk.Button(
            self.parent, text='Search', command=lambda: self.search_name(self.namev.get()))

        self.labelatm.config(state='disabled')
        self.labelsym.config(state='disabled')
        self.labelnam.config(state='disabled')

        self.btnatm.config(state='disabled')
        self.btnsym.config(state='disabled')
        self.btnnam.config(state='disabled')

        atomic.place(x=190, y=200)
        self.labelatm.place(x=310, y=200)
        self.btnatm.place(x=450, y=198)

        symbol.place(x=190, y=250)
        self.labelsym.place(x=310, y=250)
        self.btnsym.place(x=450, y=248)

        name.place(x=190, y=300)
        self.labelnam.place(x=310, y=300)
        self.btnnam.place(x=450, y=298)

    def atm_fun(self):
        self.labelatm.delete(0, tk.END)
        self.labelsym.delete(0, tk.END)
        self.labelnam.delete(0, tk.END)

        self.labelatm.config(state='normal')
        self.labelsym.config(state='disabled')
        self.labelnam.config(state='disabled')
        self.btnatm.config(state='normal')
        self.btnsym.config(state='disabled')
        self.btnnam.config(state='disabled')

    def sym_fun(self):
        self.labelatm.delete(0, tk.END)
        self.labelsym.delete(0, tk.END)
        self.labelnam.delete(0, tk.END)

        self.labelsym.config(state='normal')
        self.labelatm.config(state='disabled')
        self.labelnam.config(state='disabled')
        self.btnsym.config(state='normal')
        self.btnatm.config(state='disabled')
        self.btnnam.config(state='disabled')

    def nam_fun(self):
        self.labelatm.delete(0, tk.END)
        self.labelsym.delete(0, tk.END)
        self.labelnam.delete(0, tk.END)

        self.labelnam.config(state='normal')
        self.labelatm.config(state='disabled')
        self.labelsym.config(state='disabled')
        self.btnnam.config(state='normal')
        self.btnsym.config(state='disabled')
        self.btnatm.config(state='disabled')
