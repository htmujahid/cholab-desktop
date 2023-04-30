import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


class Info(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_info_tab()

    def create_info_tab(self):
        self.parent.configure(background='white')
        style = ttk.Style(self.parent)
        style.configure('TLabel', background='white', foreground='black')
        heading1 = ttk.Label(self.parent, text='Atomic Number:',
                            font=('Arial', 11, 'bold'))
        heading1.grid(row=0, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''Atomic number is the number of protons or electron in that element. It is unique.''')
        label1.grid(row=0, column=1, sticky='w')
        heading2 = ttk.Label(self.parent, text='Atomic Mass:',
                            font=('Arial', 11, 'bold'))
        heading2.grid(row=1, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''Atomic mass is the sum of number of nuetrons and number of protons in an element.''')
        label1.grid(row=1, column=1, sticky='w')
        heading3 = ttk.Label(self.parent, text='Period:',
                            font=('Arial', 11, 'bold'))
        heading3.grid(row=2, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''A period in the periodic table is a row of chemical elements.''')
        label1.grid(row=2, column=1, sticky='w')
        heading4 = ttk.Label(self.parent, text='Group:',
                            font=('Arial', 11, 'bold'))
        heading4.grid(row=3, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''A group in the periodic table is a column of chemical elements.''')
        label1.grid(row=3, column=1, sticky='w')
        heading5 = ttk.Label(
            self.parent, text='Neutron Number:', font=('Arial', 11, 'bold'))
        heading5.grid(row=4, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''Neutron number is the number of neutron in any chemical element''')
        label1.grid(row=4, column=1, sticky='w')
        heading6 = ttk.Label(self.parent, text='Block:',
                            font=('Arial', 11, 'bold'))
        heading6.grid(row=5, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''A set of elements having their differentiating electrons predominately in the same type of atomic orbital.''')
        label1.grid(row=5, column=1, sticky='w')
        heading7 = ttk.Label(self.parent, text='Description:',
                            font=('Arial', 11, 'bold'))
        heading7.grid(row=6, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''The physical structure of an element''')
        label1.grid(row=6, column=1, sticky='w')
        heading8 = ttk.Label(self.parent, text='Appearance:',
                            font=('Arial', 11, 'bold'))
        heading8.grid(row=7, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''The physical structure of an element''')
        label1.grid(row=7, column=1, sticky='w')
        heading9 = ttk.Label(self.parent, text='Melting Point:',
                            font=('Arial', 11, 'bold'))
        heading9.grid(row=8, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''The melting point of an element is the temperature at which it changes state from solid to liquid.''')
        label1.grid(row=8, column=1, sticky='w')
        heading10 = ttk.Label(
            self.parent, text='Boiling Point:', font=('Arial', 11, 'bold'))
        heading10.grid(row=9, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''The boiling point of an element is the temperature at which it changes state from liquid to gas.''')
        label1.grid(row=9, column=1, sticky='w')
        heading11 = ttk.Label(self.parent, text='Phase:',
                             font=('Arial', 11, 'bold'))
        heading11.grid(row=10, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''The physical structure of an element''')
        label1.grid(row=10, column=1, sticky='w')
        heading12 = ttk.Label(self.parent, text='Structure:',
                             font=('Arial', 11, 'bold'))
        heading12.grid(row=11, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''The physical structure of an element''')
        label1.grid(row=11, column=1, sticky='w')
        heading13 = ttk.Label(
            self.parent, text='Oxidation State:', font=('Arial', 11, 'bold'))
        heading13.grid(row=12, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''A number assigned to an element in chemical reaction which represents the number of electrons lost or gain.''')
        label1.grid(row=12, column=1, sticky='w')
        heading14 = ttk.Label(
            self.parent, text='Ionization Energy(I.E):', font=('Arial', 11, 'bold'))
        heading14.grid(row=13, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''Ionization Energy is the minimum amount of energy required to remove the most loosely bound electron''')
        label1.grid(row=13, column=1, sticky='w')
        heading15 = ttk.Label(
            self.parent, text='Atomic Radius:', font=('Arial', 11, 'bold'))
        heading15.grid(row=14, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''The atomic radius of a chemical element is a measure of the size of its atoms.''')
        label1.grid(row=14, column=1, sticky='w')
        heading16 = ttk.Label(
            self.parent, text='Covalent Radius:', font=('Arial', 11, 'bold'))
        heading16.grid(row=15, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''Covalent radius is half of the internuclear separation between the nuclei of two single-bonded atoms.''')
        label1.grid(row=15, column=1, sticky='w')
        heading17 = ttk.Label(
            self.parent, text='Electron Affinity(E.A):', font=('Arial', 11, 'bold'))
        heading17.grid(row=16, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''Electron affinity is the energy released when 1 mole of neutral atoms of an element receives one electron.''')
        label1.grid(row=16, column=1, sticky='w')
        heading18 = ttk.Label(
            self.parent, text='Electronegativity:', font=('Arial', 11, 'bold'))
        heading18.grid(row=17, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''Electronegativity describes the tendency of an atom to attract a shared pair of electrons towards itself.''')
        label1.grid(row=17, column=1, sticky='w')
        heading19 = ttk.Label(self.parent, text='Isotope:',
                             font=('Arial', 11, 'bold'))
        heading19.grid(row=18, column=0, sticky='w')
        label1 = ttk.Label(
            self.parent, text='''The element which have same number of protons but different number of neutrons.''')
        label1.grid(row=18, column=1, sticky='w')
