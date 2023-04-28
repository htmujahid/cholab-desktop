import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


class Help(tk.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.create_help_tab()

    def create_help_tab(self):
        heading1 = tk.Label(self.parent,text='Contact', font=('Arial', 15))
        heading1.grid(row=0,column=0,sticky='w')

        labelone = tk.Label(self.parent,justify='left',text='''Their are six main tabs of this application.                                                                                                                                              
    1.  Home: in this tab you can view all the properties by simply clicking on the name of element in periodic table.                                                  
    2.  Search: in this tab you can manually search an element by symbol, name and atomic number of that element                                   
    3.  Periodic Table: this is a periodic table tab you can simply arrange the periodic table by different properties by clicking                                     
    4.  Info: in this tab their is general idea about every chemical property which is used in app                                                
    5.  About: this is a general purpose tab in which their is a self introduction of app developer                                                                       
    6.  Help: this is the last tab for help of users...                                                                                                                                        ''')
        labelone.grid(row=1,column=0,sticky='w')