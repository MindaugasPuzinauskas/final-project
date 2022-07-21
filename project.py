from tkinter import *
import tkinter
from tkinter import ttk
from click import command

class skaiciuokles:
    def __init__(self,langas):
        notebook_tab=ttk.Notebook(langas)
        notebook_tab.pack()

        frame1= Frame(notebook_tab, width=500, height=500, bg="grey")
        frame2= Frame(notebook_tab, width=500, height=500, bg="grey")
        frame3=Frame(notebook_tab, width=500, height=500, bg="grey")
        frame4=Frame(notebook_tab, width=500, height=500, bg="grey")

        frame1.pack(fill="both", expand=1)
        frame2.pack(fill="both", expand=1)
        frame3.pack(fill="both", expand=1)
        frame4.pack(fill="both", expand=1)


        notebook_tab.add(frame1, text="KMI Skaičiuoklė")
        notebook_tab.add(frame2, text="KCAL Skaičiuoklė")
        notebook_tab.add(frame3, text="Kiek reikia išgerti vandens?")
        notebook_tab.add(frame4, text="Maisto produktų KCAL skaičiuoklė")

        vcmd_frame1=frame1.register(self.validate)
        question1= Label(frame1, text="Įveskite savo svorį kilogramais: ", justify=CENTER, anchor='w')
        question1.grid(sticky=W, column=0, row=0)

        self.svoris_frame1= Entry(frame1, validate="key",validatecommand=(vcmd_frame1,'%P'))
        self.svoris_frame1.grid(column=0, row=2)

        question2= Label(frame1, text="Įveskite savo ūgį centimetrais: ", justify=CENTER, anchor='w')
        question2.grid(sticky=W, column=0, row=4)

        self.ugis= Entry(frame1, validate="key",validatecommand=(vcmd_frame1,'%P'))
        self.ugis.grid(column=0, row=5)

        self.mygtukas1= tkinter.Button(frame1, text= "Skaičiuoti KMI", command=lambda: self.kmi())
        self.mygtukas1.grid(column=0,row=8, sticky='E')

        self.r= IntVar()
        self.a=IntVar()

        Radiobutton(frame3, text="Vyras", variable=self.r, value=1).grid(column=1,row=0, sticky=W)
        Radiobutton(frame3, text="Moteris", variable=self.r, value=2).grid(column=1,row=0, sticky=E)

        question1= Label(frame3, text="Pasirinkite savo lytį: ", justify=CENTER, anchor='w')
        question1.grid(sticky=W, column=0, row=0)

        vcmd_frame3=frame3.register(self.validate)
        question2= Label(frame3, text="Įveskite savo svorį kilogramais: ", justify=CENTER, anchor='w')
        question2.grid(sticky=W, column=0, row=4)

        self.svoris_frame3= Entry(frame3, validate="key",validatecommand=(vcmd_frame3,'%P'))
        self.svoris_frame3.grid(column=0, row=5)

        self.mygtukas2= tkinter.Button(frame3, text= "Išgeriamo vandens norma", command=lambda: self.Vandens_Skaiciuokle())
        self.mygtukas2.grid(column=1,row=8,sticky='E')



        self.message_frame1=""
        self.label_text_frame1 = StringVar()
        self.label_text_frame1.set(self.message_frame1)
        self.label_frame1 = Label(frame1, textvariable=self.label_text_frame1)
        self.label_frame1.grid(row=9,columnspan=5, sticky="W")

        self.message_frame3=""
        #Sukuriamas variable
        self.label_text_frame3 = StringVar()
        #Set nustato, koks tekstas rodomas ka tik atsidarius lentele
        self.label_text_frame3.set(self.message_frame3)
        #Padarom, kad teskstas butu matomas lenteleje ir kad ji butu galima pakeisti
        self.label_frame3 = Label(frame3, textvariable=self.label_text_frame3)
        self.label_frame3.grid(row=9,columnspan=5, sticky="W")
    
    def validate(self,new_text):
        #leidzia istrinti entry reiksme
        if not new_text: 
            new_text = None
            return True
        #leidzia ivesti tik sveikus skaicius
        if new_text:
            try:
             float(new_text)
             return True
            except ValueError:
             return False
    def kmi(self):
        #si funkcijos dalis skirta identifikuoti neivestas reiksmes
        if len(self.svoris_frame1.get())==0 and len(self.ugis.get())==0:
            self.message_frame1="Neįvestas ūgis ir svoris"
        elif len(self.svoris_frame1.get())==0:
            self.message_frame1="Neįvestas svoris"
        elif len(self.ugis.get())==0:
            self.message_frame1="Neįvestas ūgis"
        else:

            kmi=round(float(self.svoris_frame1.get())/((float(self.ugis.get())/100)**2), 2)
            if kmi <= 18.5:
                komentaras = ("Tai reiškia, kad Jūsų svoris yra nepakankamas")
            elif kmi >18.5 and kmi <=25:
                komentaras = ("Tai reiškia, kad Jūsų svoris yra normalus")
            elif kmi >25 and kmi <=30:
                komentaras = ("Tai reiškia, kad Jūs turite antsvorį")
            elif kmi >30:
                komentaras = ("Tai reiškia, kad Jūs turite 3 lygio nutukimą")
            self.message_frame1=f"Jūsų KMI yra: {kmi}. {komentaras}."
        self.label_text_frame1.set(self.message_frame1)

    def Vandens_Skaiciuokle(self):
    
        if not self.r.get() and  len(self.svoris_frame3.get())==0:
            self.message_frame3="Nepasirinkta lytis ir neįvestas svoris"
        elif not self.r.get():
            self.message_frame3 = "Nepasirinkta lytis"
        elif  len(self.svoris_frame3.get())==0:
            self.message_frame3 = "Neįvestas svoris"
        else:
        #1- vyras, 2-moteris
            pasirinkimas=self.r.get()
            if pasirinkimas==1:
                rezultatas = round((float(self.svoris_frame3.get()) * 0.035), 2)
            elif pasirinkimas==2:
                rezultatas= round((float(self.svoris_frame3.get()) * 0.037), 2)
            self.message_frame3=f"Jums reikalingo išgerti vandens paros norma yra {rezultatas} l vandens"
        self.label_text_frame3.set(self.message_frame3)
        


root1= Tk()
langas1=skaiciuokles(root1)
root1.title("Skaičiuoklė")
root1.geometry("800x400")
root1.mainloop()







        #BMA apskaiciavimo formule
        # For women, BMR = 655.1 + (9.563 x weight in kg) + (1.850 x height in cm) - (4.676 x age in years)
        # For men, BMR = 66.47 + (13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)