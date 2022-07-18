from tkinter import *
import tkinter

#Formule skirta apskaiciuoti zmogaus Kuno Mases indeksa
def kmi(self):

        if len(self.svoris.get())==0 and len(self.ugis.get())==0:
            self.message="Neįvestas ūgis ir svoris"
        elif len(self.svoris.get())==0:
            self.message="Neįvestas svoris"
        elif len(self.ugis.get())==0:
            self.message="Neįvestas ūgis"
        else:

            kmi=round(float(self.svoris.get())/((float(self.ugis.get())/100)**2), 2)
            if kmi <= 18.5:
                komentaras = ("Tai reiškia, kad Jūsų svoris yra nepakankamas")
            elif kmi >18.5 and kmi <=25:
                komentaras = ("Tai reiškia, kad Jūsų svoris yra normalus")
            elif kmi >25 and kmi <=30:
                komentaras = ("Tai reiškia, kad Jūs turite antsvorį")
            elif kmi >30:
                komentaras = ("Tai reiškia, kad Jūs turite 3 lygio nutukimą")
            self.message=f"Jūsų KMI yra: {kmi}. {komentaras}."
        self.label_text.set(self.message)


def validate(self,new_text):

    if not new_text: 
        new_text = None
        return True

    if new_text:
        try:
            float(new_text)
            return True
        except ValueError:
            return False
             
#Funkcija skirta apskaiciuoti isgeriamo vandens norma

def Vandens_Skaiciuokle(self):
    
    
    if not self.r.get() and  len(self.svoris.get())==0:
        self.message="Nepasirinkta lytis ir neįvestas svoris"
    elif not self.r.get():
        self.message = "Nepasirinkta lytis"
    elif  len(self.svoris.get())==0:
        self.message = "Neįvestas svoris"
    else:
    #1- vyras, 2-moteris
        pasirinkimas=self.r.get()
        if pasirinkimas==1:
            rezultatas = round((float(self.svoris.get()) * 0.035), 2)
        elif pasirinkimas==2:
            rezultatas= round((float(self.svoris.get()) * 0.037), 2)
        self.message=f"Jums reikalingo išgerti vandens paros norma yra {rezultatas} l vandens"
    self.label_text.set(self.message)



        #BMA apskaiciavimo formule
        # For women, BMR = 655.1 + (9.563 x weight in kg) + (1.850 x height in cm) - (4.676 x age in years)
        # For men, BMR = 66.47 + (13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)


