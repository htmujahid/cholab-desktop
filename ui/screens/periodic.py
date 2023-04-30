import os
import tkinter as tk
from tkinter import ttk

import ui.widgets.periodic as periodic


class Periodic(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_periodic_tab()

    def create_periodic_tab(self):
        self.parent.configure(background='white')
        self.periodic = periodic.PeriodicTable(self.parent)
        self.create_control_buttons()

    def create_control_buttons(self):
        style = ttk.Style()
        style.configure('TButton', background='#ccc', foreground='black')
        atmb = ttk.Button(self.parent, text='''Atomic\nNumber''',
                          command=lambda: self.periodic.set_active_property('Atomic Number'))
        atmb.place(x=2, y=557, width=70)
        msnb = ttk.Button(self.parent, text='''Atomic\nMass''',
                          command=lambda: self.periodic.set_active_property('Atomic Mass'))
        msnb.place(x=74, y=557, width=70)
        atmb = ttk.Button(self.parent, text='''Phase\n ''',
                          command=lambda: self.periodic.set_active_property('Phase'))
        atmb.place(x=146, y=557, width=70)
        atmb = ttk.Button(self.parent, text='''Boiling\nPoint''',
                          command=lambda: self.periodic.set_active_property('Boiling Point'))
        atmb.place(x=218, y=557, width=70)
        atmb = ttk.Button(self.parent, text='''Melting\nPoint''',
                          command=lambda: self.periodic.set_active_property('Melting Point'))
        atmb.place(x=290, y=557, width=70)
        atmb = ttk.Button(self.parent, text='''Electro\nNegativity''',
                          command=lambda: self.periodic.set_active_property('Electronegativity'))
        atmb.place(x=362, y=557, width=70)
        atmb = ttk.Button(self.parent, text='''Electron\nAffinity''',
                          command=lambda: self.periodic.set_active_property('Electron Affinity'))
        atmb.place(x=434, y=557, width=70)
        atmb = ttk.Button(self.parent, text='''Ionization\nEnergy''',
                          command=lambda: self.periodic.set_active_property('Ionization Energy'))
        atmb.place(x=506, y=557, width=70)
        atmb = ttk.Button(self.parent, text='''Atomic\nRadius''',
                          command=lambda: self.periodic.set_active_property('Atomic Radius'))
        atmb.place(x=578, y=557, width=70)
        atmb = ttk.Button(self.parent, text='''Cvelent\nRadius''',
                          command=lambda: self.periodic.set_active_property('Covalent Radius'))
        atmb.place(x=650, y=557, width=70)
