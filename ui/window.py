import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import ui.screens.home as home
import ui.screens.search as search
import ui.screens.periodic as periodic
import ui.screens.info as info
import ui.screens.about as about
import ui.screens.help as help


class Window(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.create_splash()

    def create_splash(self):
        root = self.parent
        image_path = Image.open(os.path.join('assets', 'Background.png'))
        self.background = ImageTk.PhotoImage(image_path)
        self.backphoto = tk.Label(image=self.background)
        self.backphoto.place(x=-76, y=-115)

        image_path = Image.open(os.path.join('assets', 'GetStarted.png'))
        self.get_started_img = ImageTk.PhotoImage(image_path)
        style = ttk.Style(root)
        style.configure('g.TButton', font=(
            'Times', 30, 'bold', 'underline'), background='yellow')
        self.get_started_btn = tk.Button(
            root, image=self.get_started_img, bd=0, bg='blue', command=self.get_started)
        self.get_started_btn.place(x=500, y=200)

    def get_started(self):
        self.get_started_btn.destroy()
        self.backphoto.destroy()
        self.create_tabs()
        self.init_screens()

    def create_tabs(self):
        root = self.parent
        style = ttk.Style(root)
        style.theme_create("custom_tabs", parent="alt", settings={"lefttab.TNotebook.Tab": {"configure": {"padding": [10, 10, 10, 10]}}})
        style.theme_use("custom_tabs")
        style.configure('lefttab.TNotebook', tabposition='wn', background='white', borderwidth=0, highlightthickness=0)
        TAB_CONTROL = ttk.Notebook(root, style='lefttab.TNotebook', padding=0)

        style.configure('lefttab.TNotebook.Tab', background='white')

        self.home_tab = tk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(self.home_tab, text="\n   Home                  \n")

        self.search_tab = tk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(self.search_tab, text="\n   Search                 \n")

        self.periodic_tab = tk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(self.periodic_tab, text="\n   Periodic Table    \n")

        self.info_tab = tk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(
            self.info_tab, text="\n   Info                      \n")

        self.about_tab = tk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(self.about_tab, text="\n   About                  \n")

        self.help_tab = tk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(self.help_tab, text="\n   Help                    \n")

        TAB_CONTROL.pack(expand=1, fill="both")

    def init_screens(self):
        home.Home(self.home_tab)
        search.Search(self.search_tab)
        periodic.Periodic(self.periodic_tab)
        info.Info(self.info_tab)
        about.About(self.about_tab)
        help.Help(self.help_tab)
