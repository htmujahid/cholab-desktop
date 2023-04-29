import tkinter as tk
from tkinter import ttk


import ui.widgets.periodic as periodic


class Periodic(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_periodic_tab()

    def create_periodic_tab(self):
        theme1 = tk.PhotoImage(file='assets/theme.png')
        them1 = tk.Label(self.parent, image=theme1)
        them1.place(x=50, y=0)
        them1.image = theme1

        self.periodic = periodic.PeriodicTable(self.parent)

        self.create_control_buttons()

    def create_control_buttons(self):
        atmb = ttk.Button(self.parent, text='''Atomic\nNumber''',
                          command=lambda: self.periodic.set_active_property('Atomic Number'))
        atmb.place(x=5, y=557, width=73)
        msnb = ttk.Button(self.parent, text='''Atomic\nMass''',
                          command=lambda: self.periodic.set_active_property('Atomic Mass'))
        msnb.place(x=77, y=557, width=73)
        atmb = ttk.Button(self.parent, text='''Phase\n ''',
                          command=lambda: self.periodic.set_active_property('Phase'))
        atmb.place(x=149, y=557, width=73)
        atmb = ttk.Button(self.parent, text='''Boiling\nPoint''',
                          command=lambda: self.periodic.set_active_property('Boiling Point'))
        atmb.place(x=221, y=557, width=73)
        atmb = ttk.Button(self.parent, text='''Melting\nPoint''',
                          command=lambda: self.periodic.set_active_property('Melting Point'))
        atmb.place(x=293, y=557, width=73)
        atmb = ttk.Button(self.parent, text='''Electro\nNegativity''',
                          command=lambda: self.periodic.set_active_property('Electronegativity'))
        atmb.place(x=365, y=557, width=73)
        atmb = ttk.Button(self.parent, text='''Electron\nAffinity''',
                          command=lambda: self.periodic.set_active_property('Electron Affinity'))
        atmb.place(x=437, y=557, width=73)
        atmb = ttk.Button(self.parent, text='''Ionization\nEnergy''',
                          command=lambda: self.periodic.set_active_property('Ionization Energy'))
        atmb.place(x=509, y=557, width=73)
        atmb = ttk.Button(self.parent, text='''Atomic\nRadius''',
                          command=lambda: self.periodic.set_active_property('Atomic Radius'))
        atmb.place(x=581, y=557, width=73)
        atmb = ttk.Button(self.parent, text='''Cvelent\nRadius''',
                          command=lambda: self.periodic.set_active_property('Covalent Radius'))
        atmb.place(x=653, y=557, width=73)
