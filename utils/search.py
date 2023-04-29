import tkinter as tk
from tkinter import messagebox
from data.elements_info import elements_info

import ui.widgets.information as information


class Search(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.elements_list = [element for element in elements_info.values()]

    def search_symbol(self, symbolv):
        search_occurence = False

        for element in self.elements_list:
            if element['Symbol'] == symbolv.title():
                symbol = tk.StringVar()
                symbol.set(element['Symbol'])
                search_occurence = True
                information.InformationWindow(self.parent, symbol)
        if not search_occurence:
            messagebox.showerror("Error", "Your Entry is wrong")

    def search_name(self, namev):
        search_occurence = False

        for element in self.elements_list:
            if element['Element Name'] == namev:
                symbol = tk.StringVar()
                symbol.set(element['Symbol'])
                search_occurence = True
                information.InformationWindow(self.parent, symbol)
        if not search_occurence:
            messagebox.showerror("Error", "Your Entry is wrong")

    def search_atomic_number(self, atomicv):
        search_occurence = False
        atomicvv = tk.StringVar()
        atomicvv.set(atomicv)
        for element in self.elements_list:
            if element['Atomic Number'] == atomicv:
                symbol = tk.StringVar()
                symbol.set(element['Symbol'])
                search_occurence = True
                information.InformationWindow(self.parent, symbol)
        if not search_occurence:
            messagebox.showerror("Error", "Your Entry is wrong")
