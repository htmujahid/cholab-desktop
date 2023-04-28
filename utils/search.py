import tkinter as tk
from tkinter import messagebox
from data.elements_info import elements_info

class Search(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.elements = elements_info
        self.elements_list = [element for element in elements_info.values()]

    def search_symbol(self, symbolv):
        hint = False
        
        for element in self.elements_list:
        
            if element['Symbol'] == symbolv.get().title():
                atmnb = tk.StringVar()
                atmnb.set(element['Symbol'])
                hint = True
                self.search_window(atmnb)
        if not hint:
            messagebox.showerror("Error","Your Entry is wrong") 

    def search_name(self, namev):
        hint = False
        
        for element in self.elements_list:
        
            if element['Element Name'] == namev.get():
                atmnb = tk.StringVar()
                atmnb.set(element['Symbol'])
                hint = True
                self.search_window(atmnb)
        if not hint:
            messagebox.showerror("Error","Your Entry is wrong")

    def search_atomic_number(self, atomicv):
        hint = False
        atomicvv = tk.StringVar()
        atomicvv.set(atomicv)
        
        for element in self.elements_list:
        
            if element['Atomic Number'] == atomicvv.get():
                atmnb = tk.StringVar()
                atmnb.set(element['Symbol'])
                hint = True
                self.search_window(atmnb)
        if not hint:
            messagebox.showerror("Error","Your Entry is wrong")

    def search_window(self, symbolv):
        symbolr = tk.Tk()
        symbolr.geometry('495x550+350+130')
        symbolr.minsize(495,550)
        symbolr.maxsize(495,550)
        heading = tk.Label(symbolr, text='INFORMATION',font=('Arial',35))
        heading.place(x=0,y=0)
        labelframe1 = tk.LabelFrame(symbolr, text="General Information")
        labelframe1.place(x=5,y=50, height=150, width=485)

        #name
        elename = tk.Label(labelframe1, text='Element Name')
        elename.place(x=0,y=0)
        elenamee = tk.Entry(labelframe1)
        elenamee.insert(0, self.elements[symbolv.get()]['Element Name'])
        elenamee.place(x=100,y=0)
        #symbole
        elesym = tk.Label(labelframe1, text='Symbol')
        elesym.place(x=250, y=0)
        elesyme = tk.Entry(labelframe1)
        elesyme.insert(0, symbolv.get())
        elesyme.place(x=350, y=0)
        #Atomic Number
        eleatn = tk.Label(labelframe1, text='Atomic Number')
        eleatn.place(x=0, y=25)
        eleatne = tk.Entry(labelframe1)
        eleatne.insert(0, self.elements[symbolv.get()]['Atomic Number'])
        eleatne.place(x=100, y=25)
        #atomic mass
        eleatm = tk.Label(labelframe1, text='Atomic Mass')
        eleatm.place(x=250, y=25)
        eleatme = tk.Entry(labelframe1)
        eleatme.insert(0, self.elements[symbolv.get()]['Atomic Mass'])
        eleatme.place(x=350, y=25)
        #Period
        eleper = tk.Label(labelframe1, text='Period')
        eleper.place(x=0, y=50)
        elepere = tk.Entry(labelframe1)
        elepere.insert(0, self.elements[symbolv.get()]['Period'])
        elepere.place(x=100, y=50)
        #group
        elegrp = tk.Label(labelframe1, text='Group')
        elegrp.place(x=250, y=50)
        elegrpe = tk.Entry(labelframe1)
        elegrpe.insert(0, self.elements[symbolv.get()]['Group'])
        elegrpe.place(x=350, y=50)
        #Neutron
        ntr = tk.IntVar()
        ntr = int(float(self.elements[symbolv.get()]['Atomic Mass']))-int(self.elements[symbolv.get()]['Atomic Number'])
        elentr = tk.Label(labelframe1, text='Neutron Number')
        elentr.place(x=0, y=75)
        elentre = tk.Entry(labelframe1)
        elentre.insert(0, ntr)
        elentre.place(x=100, y=75)
        #Block
        eleblc = tk.Label(labelframe1, text='Block')
        eleblc.place(x=250, y=75)
        eleblce = tk.Entry(labelframe1)
        eleblce.insert(0,self.elements[symbolv.get()]['block'])
        eleblce.place(x=350, y=75)
        #description
        eledes = tk.Label(labelframe1,text='Description')
        eledes.place(x=0,y=100)
        eledese = tk.Entry(labelframe1)
        eledese.insert(0, self.elements[symbolv.get()]['Description'])
        eledese.place(x=100,y=100)
        #Appearance
        eleapr = tk.Label(labelframe1, text='Appearance')
        eleapr.place(x=250, y=100)
        eleapre = tk.Entry(labelframe1)
        eleapre.insert(0, self.elements[symbolv.get()]['Appearance'])
        eleapre.place(x=350,y=100)
        labelframe2 = tk.LabelFrame(symbolr, text='Physical Properties')
        labelframe2.place(x=5,y=202, height=75, width=485)
        elemel = tk.Label(labelframe2, text='Melting Point C')
        elemel.place(x=0,y=0)
        elemele = tk.Entry(labelframe2)
        elemele.insert(0, self.elements[symbolv.get()]['Melting Point'])
        elemele.place(x=100,y=0)
        elebol = tk.Label(labelframe2, text='Boiling Point C')
        elebol.place(x=250,y=0)
        elebole = tk.Entry(labelframe2)
        elebole.insert(0, self.elements[symbolv.get()]['Boiling Point'])
        elebole.place(x=350, y=0)
        elephs = tk.Label(labelframe2, text='Phase')
        elephs.place(x=0,y=25)
        elephse = tk.Entry(labelframe2)
        elephse.insert(0, self.elements[symbolv.get()]['Phase'])
        elephse.place(x=100, y=25)
        elestr = tk.Label(labelframe2, text='Structure')
        elestr.place(x=250,y=25)
        elestre = tk.Entry(labelframe2)
        elestre.insert(0, self.elements[symbolv.get()]['Structure'])
        elestre.place(x=350,y=25)
        labelframe3 = tk.LabelFrame(symbolr,text='Atomic Poroperties')
        labelframe3.place(x=5, y=280, width= 485, height= 100)
        eleoxi = tk.Label(labelframe3, text='Oxidation State')
        eleoxi.place(x=0,y=0)
        eleoxie = tk.Entry(labelframe3)
        eleoxie.insert(0,self.elements[symbolv.get()]['Oxidation States'])
        eleoxie.place(x=100,y=0)
        eleion = tk.Label(labelframe3, text='I.E (KJ/mol)')
        eleion.place(x=250, y=50)
        eleione = tk.Entry(labelframe3)
        eleione.insert(0, self.elements[symbolv.get()]['Ionization Energy'])
        eleione.place(x=350,y=50)
        eleard = tk.Label(labelframe3, text='Atomic Rad (pm)')
        eleard.place(x=0, y=25)
        elearde = tk.Entry(labelframe3)
        elearde.insert(0, self.elements[symbolv.get()]['Atomic Radius'])
        elearde.place(x=100, y=25)
        elecrd = tk.Label(labelframe3, text='Cov Rad (pm)')
        elecrd.place(x=250, y=25)
        elecrde = tk.Entry(labelframe3)
        elecrde.insert(0, self.elements[symbolv.get()]['Covalent Radius'])
        elecrde.place(x=350, y=25)
        eleelf = tk.Label(labelframe3, text='E.A (KJ/mol)')
        eleelf.place(x=0, y=50)
        eleelfe = tk.Entry(labelframe3)
        eleelfe.insert(0, self.elements[symbolv.get()]['Electron Affinity'])
        eleelfe.place(x=100, y=50)
        eleeln = tk.Label(labelframe3, text='Electronegativity')
        eleeln.place(x=250, y=0)
        eleelne = tk.Entry(labelframe3)
        eleelne.insert(0, self.elements[symbolv.get()]['Electronegativity'])
        eleelne.place(x=350, y=0)
        labelframe4 = tk.LabelFrame(symbolr, text='History')
        labelframe4.place(x=5,y=382, width=485, height=75)
        eledis = tk.Label(labelframe4, text='Discovered By')
        eledis.place(x=0, y=0)
        eledise = tk.Entry(labelframe4)
        eledise.insert(0, self.elements[symbolv.get()]['Discovered By'])
        eledise.place(x=100,y=0)
        elenam = tk.Label(labelframe4, text='Discovered Year')
        elenam.place(x=250, y=0)
        elename = tk.Entry(labelframe4)
        elename.insert(0, self.elements[symbolv.get()]['Discovered Year'])
        elename.place(x=350,y=0)
        eleorg = tk.Label(labelframe4, text='Origin')
        eleorg.place(x=0, y=25)
        eleorge = tk.Entry(labelframe4, width=62)
        eleorge.insert(0, self.elements[symbolv.get()]['Origin'])
        eleorge.place(x=100,y=25)
        labelframe5 = tk.LabelFrame(symbolr, text='Interesting Information')
        labelframe5.place(x=5,y=460, width=230, height=70)
        i_info = tk.StringVar()
        i_info = self.elements[symbolv.get()]['i-info']
        eleinf = tk.Label(labelframe5, text=i_info)
        eleinf.place(x=0,y=0)
        labelframe6 = tk.LabelFrame(symbolr, text='Isotopes')
        labelframe6.place(x=260,y=460, width=230, height=40)
        iso = tk.StringVar()
        iso =  self.elements[symbolv.get()]['Isotopes']
        eleiso = tk.Label(labelframe6, text=iso)
        eleiso.place(x=0,y=0)
        okbtn = tk.Button(symbolr, text='''                                  OK                                  ''')
        okbtn.config(command=symbolr.destroy)
        okbtn.place(x=260,y=503)
        symbolr.mainloop()