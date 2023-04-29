import tkinter as tk
from tkinter import ttk

from data.elements_info import elements_info
from data.elements_position import elements_position

import utils.search as search


class PeriodicTable(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.active_property = 'Atomic Number'
        self.search = search.Search(self.parent)
        self.search_symbol = self.search.search_symbol
        self.elements = []
        self.create_periodic_table()

    def create_periodic_table(self):
        root = self.parent

        self.configure_styles()

        for element_position in elements_position:
            el = ttk.Button(self.parent, text=(self.get_element_text(element_position)),
                            style=element_position['style'], command=lambda: self.search_symbol(element_position['symbol']))
            el.place(x=element_position['x'], y=element_position['y'])
            self.elements.append(el)

    def configure_styles(self):
        stylee = ttk.Style()
        stylee.configure('e.TButton', background='#0E8A00',
                         foreground='#0E8A00', width=5)
        styley = ttk.Style()
        styley.configure('y.TButton', background='#9B870C',
                         foreground='#9B870C', width=5)
        styleo = ttk.Style()
        styleo.configure('o.TButton', background='#ff8c00',
                         foreground='#ff8c00', width=5)
        stylep = ttk.Style()
        stylep.configure('p.TButton', background='#e75480',
                         foreground='#e75480', width=5)

    def get_element_text(self, element_position):
        return elements_info[element_position['symbol']]['Symbol'] + '\n' + elements_info[element_position['symbol']][self.active_property]

    def set_active_property(self, active_property):
        self.active_property = active_property
        for index, element_position in enumerate(elements_position):
            self.elements[index].configure(
                text=self.get_element_text(element_position))
