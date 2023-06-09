import tkinter as tk

from data.elements_info import elements_info


class InformationWindow():
    def __init__(self, symbolv):
        self.symbolv = symbolv
        self.elements = elements_info
        self.create_information_window()

    def create_information_window(self):
        symbolr = tk.Tk()
        symbolr.geometry('495x550+350+130')
        symbolr.minsize(495, 550)
        symbolr.maxsize(495, 550)
        symbolr.configure(background='#ffffff')
        symbolr.resizable(False, False)

        heading = tk.Label(symbolr, text='INFORMATION', font=('Arial', 35))
        heading.configure(foreground='#000000', background='white')
        heading.place(x=0, y=0)

        labelframe1 = tk.LabelFrame(symbolr, text="General Information")
        labelframe1.configure(background='#ffffff', foreground='#000000')
        labelframe1.place(x=5, y=50, height=150, width=485)

        # name
        elename = tk.Label(labelframe1, text='Element Name')
        elename.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elename.place(x=0, y=0)

        elenamee = tk.Entry(labelframe1)
        elenamee.insert(0, self.elements[self.symbolv.get()]['Element Name'])
        elenamee.configure(background='#ffffff', foreground='#000000', width=13)
        elenamee.place(x=105, y=0)

        # symbole
        elesym = tk.Label(labelframe1, text='Symbol')
        elesym.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elesym.place(x=240, y=0)
        elesyme = tk.Entry(labelframe1)
        elesyme.insert(0, self.symbolv.get())
        elesyme.configure(background='#ffffff', foreground='#000000', width=13)
        elesyme.place(x=345, y=0)
        # Atomic Number
        eleatn = tk.Label(labelframe1, text='Atomic Number')
        eleatn.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleatn.place(x=0, y=25)
        eleatne = tk.Entry(labelframe1)
        eleatne.insert(0, self.elements[self.symbolv.get()]['Atomic Number'])
        eleatne.configure(background='#ffffff', foreground='#000000', width=13)
        eleatne.place(x=105, y=25)
        # atomic mass
        eleatm = tk.Label(labelframe1, text='Atomic Mass')
        eleatm.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleatm.place(x=240, y=25)
        eleatme = tk.Entry(labelframe1)
        eleatme.insert(0, self.elements[self.symbolv.get()]['Atomic Mass'])
        eleatme.configure(background='#ffffff', foreground='#000000', width=13)
        eleatme.place(x=345, y=25)
        # Period
        eleper = tk.Label(labelframe1, text='Period')
        eleper.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleper.place(x=0, y=50)
        elepere = tk.Entry(labelframe1)
        elepere.insert(0, self.elements[self.symbolv.get()]['Period'])
        elepere.configure(background='#ffffff', foreground='#000000', width=13)
        elepere.place(x=105, y=50)
        # group
        elegrp = tk.Label(labelframe1, text='Group')
        elegrp.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elegrp.place(x=240, y=50)
        elegrpe = tk.Entry(labelframe1)
        elegrpe.insert(0, self.elements[self.symbolv.get()]['Group'])
        elegrpe.configure(background='#ffffff', foreground='#000000', width=13)
        elegrpe.place(x=345, y=50)
        # Neutron
        ntr = tk.IntVar()
        ntr = int(float(self.elements[self.symbolv.get()]['Atomic Mass'])) - \
            int(self.elements[self.symbolv.get()]['Atomic Number'])
        elentr = tk.Label(labelframe1, text='Neutron Number')
        elentr.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elentr.place(x=0, y=75)
        elentre = tk.Entry(labelframe1)
        elentre.insert(0, ntr)
        elentre.configure(background='#ffffff', foreground='#000000', width=13)
        elentre.place(x=105, y=75)
        # Block
        eleblc = tk.Label(labelframe1, text='Block')
        eleblc.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleblc.place(x=240, y=75)
        eleblce = tk.Entry(labelframe1)
        eleblce.insert(0, self.elements[self.symbolv.get()]['block'])
        eleblce.configure(background='#ffffff', foreground='#000000', width=13)
        eleblce.place(x=345, y=75)
        # description
        eledes = tk.Label(labelframe1, text='Description')
        eledes.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eledes.place(x=0, y=100)
        eledese = tk.Entry(labelframe1)
        eledese.insert(0, self.elements[self.symbolv.get()]['Description'])
        eledese.configure(background='#ffffff', foreground='#000000', width=13)
        eledese.place(x=105, y=100)
        # Appearance
        eleapr = tk.Label(labelframe1, text='Appearance')
        eleapr.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleapr.place(x=240, y=100)
        eleapre = tk.Entry(labelframe1)
        eleapre.insert(0, self.elements[self.symbolv.get()]['Appearance'])
        eleapre.configure(background='#ffffff', foreground='#000000', width=13)
        eleapre.place(x=345, y=100)

        labelframe2 = tk.LabelFrame(symbolr, text='Physical Properties')
        labelframe2.configure(background='#ffffff', foreground='#000000')
        labelframe2.place(x=5, y=202, height=75, width=485)
        elemel = tk.Label(labelframe2, text='Melting Point C')
        elemel.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elemel.place(x=0, y=0)
        elemele = tk.Entry(labelframe2)
        elemele.insert(0, self.elements[self.symbolv.get()]['Melting Point'])
        elemele.configure(background='#ffffff', foreground='#000000', width=13)
        elemele.place(x=105, y=0)
        elebol = tk.Label(labelframe2, text='Boiling Point C')
        elebol.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elebol.place(x=240, y=0)
        elebole = tk.Entry(labelframe2)
        elebole.insert(0, self.elements[self.symbolv.get()]['Boiling Point'])
        elebole.configure(background='#ffffff', foreground='#000000', width=13)
        elebole.place(x=345, y=0)
        elephs = tk.Label(labelframe2, text='Phase')
        elephs.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elephs.place(x=0, y=25)
        elephse = tk.Entry(labelframe2)
        elephse.insert(0, self.elements[self.symbolv.get()]['Phase'])
        elephse.configure(background='#ffffff', foreground='#000000', width=13)
        elephse.place(x=105, y=25)
        elestr = tk.Label(labelframe2, text='Structure')
        elestr.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elestr.place(x=240, y=25)
        elestre = tk.Entry(labelframe2)
        elestre.insert(0, self.elements[self.symbolv.get()]['Structure'])
        elestre.configure(background='#ffffff', foreground='#000000', width=13)
        elestre.place(x=345, y=25)
        labelframe3 = tk.LabelFrame(symbolr, text='Atomic Poroperties')
        labelframe3.configure(background='#ffffff', foreground='#000000')
        labelframe3.place(x=5, y=280, width=485, height=100)
        eleoxi = tk.Label(labelframe3, text='Oxidation State')
        eleoxi.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleoxi.place(x=0, y=0)
        eleoxie = tk.Entry(labelframe3)
        eleoxie.insert(
            0, self.elements[self.symbolv.get()]['Oxidation States'])
        eleoxie.configure(background='#ffffff', foreground='#000000', width=13)
        eleoxie.place(x=105, y=0)
        eleion = tk.Label(labelframe3, text='I.E (KJ/mol)')
        eleion.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleion.place(x=240, y=50)
        eleione = tk.Entry(labelframe3)
        eleione.insert(
            0, self.elements[self.symbolv.get()]['Ionization Energy'])
        eleione.configure(background='#ffffff', foreground='#000000', width=13)
        eleione.place(x=345, y=50)
        eleard = tk.Label(labelframe3, text='Atomic Rad (pm)')
        eleard.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleard.place(x=0, y=25)
        elearde = tk.Entry(labelframe3)
        elearde.insert(0, self.elements[self.symbolv.get()]['Atomic Radius'])
        elearde.configure(background='#ffffff', foreground='#000000', width=13)
        elearde.place(x=105, y=25)
        elecrd = tk.Label(labelframe3, text='Cov Rad (pm)')
        elecrd.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elecrd.place(x=240, y=25)
        elecrde = tk.Entry(labelframe3)
        elecrde.insert(0, self.elements[self.symbolv.get()]['Covalent Radius'])
        elecrde.configure(background='#ffffff', foreground='#000000', width=13)
        elecrde.place(x=345, y=25)
        eleelf = tk.Label(labelframe3, text='E.A (KJ/mol)')
        eleelf.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleelf.place(x=0, y=50)
        eleelfe = tk.Entry(labelframe3)
        eleelfe.insert(
            0, self.elements[self.symbolv.get()]['Electron Affinity'])
        eleelfe.configure(background='#ffffff', foreground='#000000', width=13)
        eleelfe.place(x=105, y=50)
        eleeln = tk.Label(labelframe3, text='Electronegativity')
        eleeln.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleeln.place(x=240, y=0)
        eleelne = tk.Entry(labelframe3)
        eleelne.insert(
            0, self.elements[self.symbolv.get()]['Electronegativity'])
        eleelne.configure(background='#ffffff', foreground='#000000', width=13)
        eleelne.place(x=345, y=0)
        labelframe4 = tk.LabelFrame(symbolr, text='History')
        labelframe4.configure(background='#ffffff', foreground='#000000')
        labelframe4.place(x=5, y=382, width=485, height=75)
        eledis = tk.Label(labelframe4, text='Discovered By')
        eledis.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eledis.place(x=0, y=0)
        eledise = tk.Entry(labelframe4)
        eledise.insert(0, self.elements[self.symbolv.get()]['Discovered By'])
        eledise.configure(background='#ffffff', foreground='#000000', width=13)
        eledise.place(x=105, y=0)
        elenam = tk.Label(labelframe4, text='Discovered Year')
        elenam.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        elenam.place(x=240, y=0)
        elename = tk.Entry(labelframe4)
        elename.insert(0, self.elements[self.symbolv.get()]['Discovered Year'])
        elename.configure(background='#ffffff', foreground='#000000', width=13)
        elename.place(x=345, y=0)
        eleorg = tk.Label(labelframe4, text='Origin')
        eleorg.configure(background='#ffffff', foreground='#000000', width=13, anchor='w')
        eleorg.place(x=0, y=25)
        eleorge = tk.Entry(labelframe4, width=62)
        eleorge.insert(0, self.elements[self.symbolv.get()]['Origin'])
        eleorge.configure(background='#ffffff', foreground='#000000', width=40)
        eleorge.place(x=105, y=25)
        labelframe5 = tk.LabelFrame(symbolr, text='Interesting Information')
        labelframe5.configure(background='#ffffff', foreground='#000000')
        labelframe5.place(x=5, y=460, width=240, height=60)
        i_info = tk.StringVar()
        i_info = self.elements[self.symbolv.get()]['i-info']
        eleinf = tk.Label(labelframe5, text=i_info)
        eleinf.configure(background='#ffffff', foreground='#000000', wraplength=220, justify='left')
        eleinf.place(x=0, y=0)
        labelframe6 = tk.LabelFrame(symbolr, text='Isotopes')
        labelframe6.configure(background='#ffffff', foreground='#000000')
        labelframe6.place(x=250, y=460, width=240, height=60)
        iso = tk.StringVar()
        iso = self.elements[self.symbolv.get()]['Isotopes']
        eleiso = tk.Label(labelframe6, text=iso)
        eleiso.configure(background='#ffffff', foreground='#000000', wraplength=220, justify='left')
        eleiso.place(x=0, y=0)
        okbtn = tk.Button(symbolr, text='Ok', pady=10)
        okbtn.configure(background='#ffffff', foreground='#000000', anchor='s')
        okbtn.config(command=symbolr.destroy)
        okbtn.place(x=-5, y=521, width=510, height=35)
        symbolr.mainloop()
