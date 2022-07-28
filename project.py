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
        self.frame2=frame2
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

        ################################ FRAME 1 ######################################

        vcmd_frame1=frame1.register(self.validate)
        question1= Label(frame1, text="Įveskite savo svorį kilogramais: ", justify=CENTER, anchor='w')
        question1.grid(sticky=W, column=0, row=0)

        self.svoris_frame1= Entry(frame1, validate="key",validatecommand=(vcmd_frame1,'%P'))
        self.svoris_frame1.grid(column=0, row=2)

        question2= Label(frame1, text="Įveskite savo ūgį centimetrais: ", justify=CENTER, anchor='w')
        question2.grid(sticky=W, column=0, row=4)

        self.ugis_frame1= Entry(frame1, validate="key",validatecommand=(vcmd_frame1,'%P'))
        self.ugis_frame1.grid(column=0, row=5)

        self.button1= tkinter.Button(frame1, text= "Skaičiuoti KMI", command=lambda: self.kmi())
        self.button1.grid(column=0,row=8, sticky='E')

        self.message_frame1=""
        #Sukuriamas variable
        self.label_text_frame1 = StringVar()
        #Set nustato, koks tekstas rodomas ka tik atsidarius lentele
        self.label_text_frame1.set(self.message_frame1)
        #Padarom, kad teskstas butu matomas lenteleje ir kad ji butu galima pakeisti
        self.label_frame1 = Label(frame1, textvariable=self.label_text_frame1)
        self.label_frame1.grid(row=9,columnspan=5, sticky="W")


        ############################ FRAME 3 #################################

        self.r= IntVar()
        self.a=IntVar()
        self.b= IntVar()

        Radiobutton(frame3, text="Vyras", variable=self.r, value=1).grid(column=1,row=0, sticky=W)
        Radiobutton(frame3, text="Moteris", variable=self.r, value=2).grid(column=1,row=0, sticky=E)

        question1= Label(frame3, text="Pasirinkite savo lytį: ", justify=CENTER, anchor='w')
        question1.grid(sticky=W, column=0, row=0)

        vcmd_frame3=frame3.register(self.validate)
        question2= Label(frame3, text="Įveskite savo svorį kilogramais: ", justify=CENTER, anchor='w')
        question2.grid(sticky=W, column=0, row=4)

        self.svoris_frame3= Entry(frame3, validate="key",validatecommand=(vcmd_frame3,'%P'))
        self.svoris_frame3.grid(column=0, row=5)

        self.button2= tkinter.Button(frame3, text= "Išgeriamo vandens norma", command=lambda: self.Vandens_Skaiciuokle())
        self.button2.grid(column=1,row=8,sticky='E')

        self.message_frame3=""
        self.label_text_frame3 = StringVar()
        self.label_text_frame3.set(self.message_frame3)
        self.label_frame3 = Label(frame3, textvariable=self.label_text_frame3)
        self.label_frame3.grid(row=9,columnspan=5, sticky="W")

        ##################### FRAME 2 #########################################
        Radiobutton(frame2, text="Vyras", variable=self.b, value=8).grid(column=0,row=1, sticky=W)
        Radiobutton(frame2, text="Moteris", variable=self.b, value=9).grid(column=0,row=1, sticky=E)

        Radiobutton(frame2, text="Priaugti", variable=self.a, value=3,command=self.interactive).grid(column=1,row=20, sticky=W)
        Radiobutton(frame2, text="Numesti", variable=self.a, value=4,command=self.interactive).grid(column=2,row=20, sticky=E)
        # self.label_text_frame2.set(self.message_frame2)

        question1= Label(frame2, text="Pasirinkite savo lytį: ", justify=CENTER, anchor='w')
        question1.grid(sticky=W, column=0, row=0)

        question2=Label(frame2, text= "Įveskite savo amžių: ", justify=LEFT, anchor="w")
        question2.grid(sticky= W, column=0, row=2)

        vcmd=frame2.register(self.validate)
        self.amzius= Entry(frame2, validate="key", validatecommand=(vcmd,'%P'))
        self.amzius.grid(column=0, row=3, sticky=W)

        vcmd_frame2=frame2.register(self.validate)
        question3= Label(frame2, text="Įveskite savo svorį kilogramais: ", justify=CENTER, anchor='w')
        question3.grid(sticky=W, column=0, row=4)
        self.svoris_frame2= Entry(frame2, validate="key",validatecommand=(vcmd_frame2,'%P'))
        self.svoris_frame2.grid(column=0, row=5)

        question3= Label(frame2, text="Įveskite savo ūgį centimetrais: ", justify=CENTER, anchor='w')
        question3.grid(sticky=W, column=0, row=6)

        self.ugis_frame2= Entry(frame2, validate="key",validatecommand=(vcmd_frame2,'%P'))
        self.ugis_frame2.grid(column=0, row=7)

        question4= Label(frame2, text= "Įveskite savo aktyvumo lygį: ", justify=LEFT, anchor="w")
        question4.grid(sticky=W, column=0, row=8)

        question5= Label(frame2, text= "Jeigu norite priaugti arba numesti svorio, pasirinkite tinkamą variantą: ", justify=LEFT, anchor="w")
        question5.grid(sticky=W, columnspan=3, row=18)

  

        self.message_frame2=""
        self.label_text_frame2 = StringVar()
        self.label_text_frame2.set(self.message_frame2)
        self.label_frame2 = Label(frame2, textvariable=self.label_text_frame2)
        self.label_frame2.grid(row=16,columnspan=5, sticky="W")

        #StringVar skirtas Option menu
        self.clicked=StringVar()
        self.clicked.set("Išskleisti")
        self.aktyvumo_pasirinkimai= OptionMenu(frame2, self.clicked, "Labai mažas (nėra treniruočių, sėdimas darbas)", "Nedidelis (lengvos treniruotės, sėdimas darbas)", "Vidutinis (sunkios treniruotės, sėdimas darbas)", "Didelis (vidutinės treniruotės, aktyvus darbas)", "Labai didelis (sunkios treniruotės, aktyvus darbas)")
        self.aktyvumo_pasirinkimai.grid(sticky=W, column=0,columnspan=2, row=9)
        #Columnspan leidzia eiti per kelis stulpelius

        self.button3= tkinter.Button(frame2, text= "Dienos kalorijų norma", command=lambda: self.Zmogaus_info())
        self.button3.grid(column=2,row=12,sticky='E')

    
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
        if len(self.svoris_frame1.get())==0 and len(self.ugis_frame1.get())==0:
            self.message_frame1="Neįvestas ūgis ir svoris"
        elif len(self.svoris_frame1.get())==0:
            self.message_frame1="Neįvestas svoris"
        elif len(self.ugis_frame1.get())==0:
            self.message_frame1="Neįvestas ūgis"
        else:

            kmi=round(float(self.svoris_frame1.get())/((float(self.ugis_frame1.get())/100)**2), 2)
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

    def Zmogaus_info(self):        
        
        if not self.b.get() or len(self.ugis_frame2.get())==0 or len(self.svoris_frame2.get())==0 or len(self.amzius.get())==0 or self.clicked.get()=="Išskleisti":
            neivesta=[]

            if not self.b.get():
                neivesta.append("Neįvesta lytis")

            if len(self.ugis_frame2.get())==0:
                neivesta.append("neįvestas ūgis")

            if len(self.svoris_frame2.get())==0:
                neivesta.append("neįvestas svoris")

            if len(self.amzius.get())==0:
                neivesta.append("neįvestas amžius")

            if self.clicked.get()=="Išskleisti":
                neivesta.append("nepasirinktas aktyvumo lygis")
            self.message_frame2=(', '.join(neivesta))

        else:

            lytis=float(self.b.get())
            
            
            if lytis==8:
                x=66
                xu=5.003*float(self.ugis_frame2.get())
                xs=13.75*float(self.svoris_frame2.get())
                xa=6.755*float(self.amzius.get())
                BMA_rezulatas= x + xs + xu - xa
            elif lytis==9:
                x=655.1
                xu=1.850*float(self.ugis_frame2.get())
                xs=9.563*float(self.svoris_frame2.get())
                xa=4.676*float(self.amzius.get())
                BMA_rezulatas= x + xs + xu - xa

        

            aktyvumo_lygis = self.clicked.get()
            labai_mazas=1.2
            nedidelis= 1.375
            vidutinis= 1.55
            didelis= 1.725
            labai_didelis= 1.9

            if aktyvumo_lygis== "Labai mažas (nėra treniruočių, sėdimas darbas)":
                self.ALC=round(labai_mazas* BMA_rezulatas)
            elif aktyvumo_lygis== "Nedidelis (lengvos treniruotės, sėdimas darbas)":
                self.ALC=round(nedidelis*BMA_rezulatas)
            elif aktyvumo_lygis== "Vidutinis (sunkios treniruotės, sėdimas darbas)":
                self.ALC=round(vidutinis*BMA_rezulatas)
            elif aktyvumo_lygis=="Didelis (vidutinės treniruotės, aktyvus darbas)":
                self.ALC=round(didelis*BMA_rezulatas)
            elif aktyvumo_lygis== "Labai didelis (sunkios treniruotės, aktyvus darbas)":
                self.ALC=round(labai_didelis* BMA_rezulatas)
        
            
            self.message_frame2=f"Jūsų dienos kalorijų norma yra {self.ALC} Kcal"
        self.label_text_frame2.set(self.message_frame2)
        

    def interactive(self):
        
        if self.a.get()==3:
            kalorijos=self.ALC+500
            kl= Label(self.frame2, text= f"Siekiant priaugti svorio, Jūsų suvartojama dienos kalorijų normą turėtų būti {kalorijos} Kcal       ", justify=LEFT, anchor="w")
            kl.grid(sticky=W, columnspan=3, row=21)
        
        elif self.a.get()==4:
            kalorijos=self.ALC-500
            kl= Label(self.frame2, text= f"Siekiant numesti svorį, Jūsų suvartojama dienos kalorijų normą turėtų būti {kalorijos} Kcal          ", justify=LEFT, anchor="w")
            kl.grid(sticky=W, columnspan=3, row=21)


 

        

root1= Tk()
langas1=skaiciuokles(root1)
root1.title("Skaičiuoklė")
root1.geometry("800x400")
root1.mainloop()