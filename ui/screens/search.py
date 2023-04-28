import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

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
        num = tk.IntVar()

        self.namev = tk.StringVar()
        self.symbolv = tk.StringVar()
        self.atomicv = tk.StringVar()

        tab1bg = tk.PhotoImage(file='assets/Capture1.png')
        bgtab1 = tk.Label(self.parent, image=tab1bg)
        bgtab1.place(x=0, y=0)
        bgtab1.image = tab1bg

        atomic = ttk.Radiobutton(self.parent, text='Atomic Number ', variable = num, value =0, command=self.atm_fun)
        symbol = ttk.Radiobutton(self.parent, text='Symbol                ', variable = num, value = 1, command=self.sym_fun)
        name = ttk.Radiobutton(self.parent, text='Name                   ', variable = num, value = 2, command=self.nam_fun)

        self.labelatm = tk.Entry(self.parent, textvariable=self.atomicv)
        self.labelsym = tk.Entry(self.parent, textvariable=self.symbolv)
        self.labelnam = tk.Entry(self.parent, textvariable=self.namev)

        self.btnatm = tk.Button(self.parent, text='Search', command=lambda: self.search_atomic_number(self.atomicv.get()))
        self.btnsym = tk.Button(self.parent, text='Search', command=lambda: self.search_symbol(self.symbolv))
        self.btnnam = tk.Button(self.parent, text='search', command=lambda: self.search_name(self.namev))

        self.labelatm.config(state='disabled')
        self.labelsym.config(state='disabled')
        self.labelnam.config(state='disabled')

        self.btnatm.config(state='disabled')
        self.btnsym.config(state='disabled')
        self.btnnam.config(state='disabled')

        atomic.place(x=200, y=200)
        self.labelatm.place(x=310, y=200)
        self.btnatm.place(x=440, y=200)

        symbol.place(x=200, y=250)
        self.labelsym.place(x=310, y=250)
        self.btnsym.place(x=440, y=250)

        name.place(x=200, y=300)
        self.labelnam.place(x=310, y=300)
        self.btnnam.place(x=440, y=300)


    def atm_fun(self):
        self.labelatm.delete(0,tk.END)
        self.labelsym.delete(0,tk.END)
        self.labelnam.delete(0,tk.END)

        self.labelatm.config(state='normal')
        self.labelsym.config(state='disabled')
        self.labelnam.config(state='disabled')
        self.btnatm.config(state='normal')
        self.btnsym.config(state='disabled')
        self.btnnam.config(state='disabled')

    def sym_fun(self):
        self.labelatm.delete(0,tk.END)
        self.labelsym.delete(0,tk.END)
        self.labelnam.delete(0,tk.END)

        self.labelsym.config(state='normal')
        self.labelatm.config(state='disabled')
        self.labelnam.config(state='disabled')
        self.btnsym.config(state='normal')
        self.btnatm.config(state='disabled')
        self.btnnam.config(state='disabled')
        
    def nam_fun(self):
        self.labelatm.delete(0,tk.END)
        self.labelsym.delete(0,tk.END)
        self.labelnam.delete(0,tk.END)

        self.labelnam.config(state='normal')
        self.labelatm.config(state='disabled')
        self.labelsym.config(state='disabled')
        self.btnnam.config(state='normal')
        self.btnsym.config(state='disabled')
        self.btnatm.config(state='disabled')
        