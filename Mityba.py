from calendar import weekday
from tkinter import *
from tkinter import messagebox
import sqlite3
import re
from datetime import datetime
from PIL import ImageTk, Image
import tkinter
from tkinter import ttk
import tkinter as tk
import pyautogui
import csv
import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from slaptazodis import kodas

# current_username=""
current_user="emp"

class login_window:
    # current_username=""
    def __init__(self, wnd):
        self.wnd=wnd
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS record(
                            Username TEXT PRIMARY KEY,
                            Email TEXT NOT NULL UNIQUE,
                            Password TEXT,
                            DateCreated TEXT
                            
                        )
                    ''')
        con.commit()



        




        self.img_login=PhotoImage(file="login.png")
        Label(wnd, image=self.img_login, border=0, bg="white").place(x=50, y=90)

        frame=Frame(self.wnd, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        heading=Label(frame, text="Prisijungti", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=100, y=5)

        self.user= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "Username")
        self.user.bind("<FocusIn>", self.on_enter5)
        self.user.bind("<FocusOut>", self.on_leave5)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

        username_icon= Image.open('name-icon.png')
        photo= ImageTk.PhotoImage(username_icon)
        username_icon_label= Label(frame, image=photo, bg='white')
        username_icon_label.image=photo
        username_icon_label.place(x=0, y=75)

        self.passw= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11), show="*")
        self.passw.place(x=30, y=150)
        self.passw.insert(0, "Password")
        self.passw.bind("<FocusIn>", self.on_enter6)
        self.passw.bind("<FocusOut>", self.on_leave6)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

        check_button2= Checkbutton(frame, text="Rodyti slaptažodį", command=self.show_password6)
        check_button2.place(x=30, y=180)

        pass_icon3= Image.open('pass-icon.png')
        photo4= ImageTk.PhotoImage(pass_icon3)
        pass_icon_label3= Label(frame, image=photo4, bg='white')
        pass_icon_label3.image=photo4
        pass_icon_label3.place(x=0, y=150)

        #############___________SIGN IN BUTTON______________#############

        Button(frame, width=30, pady=7, text="Prisijungti", fg="#57a1f8", bg="#57a1f8", border=0, command=self.signin).place(x=35, y=215)
        label= Label(frame, text="Dar neturite paskyros?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
        label.place(x=75,y=270)

        sign_up= Button(frame, width=6, text="Registruotis", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=self.signup_command)
        sign_up.place(x=215, y=270)
        

    def signin(self):
        global current_user
        username= self.user.get()
        password=self.passw.get()

        con = sqlite3.connect('data.db')
        c = con.cursor()
        c.execute("Select * from record where username==:name", {"name":username})

        if username=="Username":
            messagebox.showerror("Ivnalid", "Įveskite slapyvardį!")
        else:

            if c.fetchone()==None:
                messagebox.showinfo("Sign up", "Slapyvardis neegzistuoja")
            else:
                c.execute("Select * from record where username==:name and password==:pwd", {"name":username, "pwd":password})
                if c.fetchone()==None:
                    messagebox.showerror("Invalid", "Neteisingas slapyvardis arba slaptažodis!")
                else:  
                    current_user=username
                    messagebox.showinfo("Signed in", "Prisijungta")
                    self.wnd.destroy()
                    
                    ######### import skaiciuoklesssssss ##############
        con.commit()

    def callback(self):
        quitting=messagebox.askokcancel("Quit", "Ar tikrai norite išeiti?")
        if quitting:
            exit()
            

    def usernameused(self):
        global current_user
        username= self.user.get()
        password=self.passw.get()

        con = sqlite3.connect('data.db')
        c = con.cursor()
        c.execute("Select * from record where username==:name", {"name":username})
        try:
            if username!="Username" and c.fetchone()!=None:
                c.execute("Select * from record where username==:name and password==:pwd", {"name":username, "pwd":password})
                if c.fetchone()!=None:
                    current_user=username
        except:
            pass
        con.commit()


    #############___________SIGN UP FORM______________#############

    def signup_command(self):
        self.window=Toplevel(self.wnd)

        self.window.title("Sign Up")
        self.window.geometry("925x500+300+200")
        self.window.configure(bg= "#fff")
        self.window.resizable(False, False)

        img_signup=PhotoImage(file="signup.png")
        Label(self.window, image=img_signup, border=0, bg="white").place(x=0, y=0)

        frame_signup=Frame(self.window, width=450, height=570, bg="#fff")
        frame_signup.place(x=480, y=50)

        heading_signup=Label(frame_signup, text="Registruotis", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23,"bold"))
        heading_signup.place(x=100, y=5)

        self.user_signup=Entry(frame_signup, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
        self.user_signup.place(x=30, y=80)
        self.user_signup.insert(0, "Username")
        self.user_signup.bind("<FocusIn>", self.on_enter1)
        self.user_signup.bind("<FocusOut>", self.on_leave1)

        Frame(frame_signup, width=295, height=2, bg="black").place(x=25, y=107)

        username_icon_signup= Image.open('name-icon.png')
        photo_signup= ImageTk.PhotoImage(username_icon_signup)
        username_icon_label_signup= Label(frame_signup, image=photo_signup, bg='white')
        username_icon_label_signup.image=photo_signup
        username_icon_label_signup.place(x=0, y=75)

        self.e_email=Entry(frame_signup, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
        self.e_email.place(x=30, y=150)
        self.e_email.insert(0, "Email")
        self.e_email.bind("<FocusIn>", self.on_enter2)
        self.e_email.bind("<FocusOut>", self.on_leave2)

        Frame(frame_signup, width=295, height=2, bg="black").place(x=25, y=177)

        email_icon= Image.open('email-icon.png')
        photo_sign= ImageTk.PhotoImage(email_icon)
        email_icon_label= Label(frame_signup, image=photo_sign, bg='white')
        email_icon_label.image=photo_sign
        email_icon_label.place(x=0, y=148)

        self.passw_signup=Entry(frame_signup, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11), show="*")
        self.passw_signup.place(x=30, y=220)
        self.passw_signup.insert(0, "Password")
        self.passw_signup.bind("<FocusIn>", self.on_enter3)
        self.passw_signup.bind("<FocusOut>", self.on_leave3)

        Frame(frame_signup, width=295, height=2, bg="black").place(x=25, y=317)

        check_button= Checkbutton(frame_signup, text="Rodyti slaptažodį", command=self.show_password3)
        check_button.place(x=30, y=250)

        pass_icon= Image.open('pass-icon.png')
        photo2= ImageTk.PhotoImage(pass_icon)
        pass_icon_label= Label(frame_signup, image=photo2, bg='white')
        pass_icon_label.image=photo2
        pass_icon_label.place(x=0, y=215)

        self.conf=Entry(frame_signup, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11), show="*")
        self.conf.place(x=30, y=290)
        self.conf.insert(0, "Confirm Password")
        self.conf.bind("<FocusIn>", self.on_enter4)
        self.conf.bind("<FocusOut>", self.on_leave4)

        Frame(frame_signup, width=295, height=2, bg="black").place(x=25, y=247)

        check_button1= Checkbutton(frame_signup, text="Rodyti slaptažodį", command=self.show_password4)
        check_button1.place(x=30, y=320)

        pass_icon2= Image.open('pass-icon.png')
        photo3= ImageTk.PhotoImage(pass_icon2)
        pass_icon_label2= Label(frame_signup, image=photo3, bg='white')
        pass_icon_label2.image=photo3
        pass_icon_label2.place(x=0, y=285)


        #############___________SIGN UP BUTTON______________#############

        Button(frame_signup, width=39, pady=7, text="Registruotis", fg="#57a1f8", bg="#57a1f8", border=0, command=self.signup).place(x=35, y=350)
        label_signup=Label(frame_signup, text="Jau turiu paskyrą", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
        label_signup.place(x=90, y=410)

        signin=Button(frame_signup, width=6, text="Prisijungti", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=self.sign)
        signin.place(x=200, y=410)



        self.window.mainloop()

    def signup(self):
        username=self.user_signup.get()
        password=self.passw_signup.get()
        confim_passw=self.conf.get()
        email= self.e_email.get()

        current_datetime=datetime.now().strftime("%B %d, %Y %I:%M%p")
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        con = sqlite3.connect('data.db')
        acur = con.cursor()
        acur.execute("Select * from record where username==:name;", {"name":username})
        if username=="Username":
            messagebox.showerror("Invalid", "Slapyvardis negali būti tuščias!")
        elif email=="Email":
            messagebox.showerror("Invalid", "El. paštas negali būti tuščias!")
        elif not re.fullmatch(email_pattern,email):
            messagebox.showerror("Invalid", "Įveskite galiojantį el.pašto adresą!")
        elif password=="Password":
            messagebox.showerror("Invalid", "Įveskite slaptažodį!")
        elif len(password)<6:
            messagebox.showerror("Invalid", "Slaptažodį turi sudaryti bent 6 simboliai!")
        else:
            
            if acur.fetchone()!=None:
                messagebox.showerror("Invalid", "Pasirinktas slapyvardis jau egzistuoja!")
            else:
                acur.execute("Select * from record where Email==:email;", {"email":email})
                if acur.fetchone()!=None:
                    messagebox.showerror("Invalid", "Pasirinktas el. paštas jau egzistruoja!")
                else:
                    if password==confim_passw:
                        acur.execute("INSERT INTO record VALUES (:name, :email, :password, :datetime)", {
                            'name': self.user_signup.get(),
                            'password': self.passw_signup.get(),
                            'email': self.e_email.get(),
                            'datetime':current_datetime})

                        messagebox.showinfo("Signup", "Sėkmingai užsiregistruota")
                        self.window.destroy()
                    else:
                        messagebox.showerror("Invalid", "Slaptažodžiai nesutampa!")
            

        con.commit()

    def sign(self):
        self.window.destroy()




    #############___________USERNAME ENTRY______________#############

    def on_enter1(self,e):
        self.user_signup.delete(0, "end")

    def on_leave1(self,e):
        if self.user_signup.get()=="":
            self.user_signup.insert(0, "Username")




    #############___________EMAIL ENTRY______________#############

    def on_enter2(self,e):
        self.e_email.delete(0, "end")

    def on_leave2(self,e):
        if self.e_email.get()=="":
            self.e_email.insert(0, "Email")
                    




    #############___________PASSWORD ENTRY______________#############
        
    def on_enter3(self,e):
        self.passw_signup.delete(0, "end")

    def on_leave3(self,e):
        if self.passw_signup.get()=="":
            self.passw_signup.insert(0, "Password")

    def show_password3(self):
        if self.passw_signup.cget('show')=='*':
            self.passw_signup.config(show='')
        else:
            self.passw_signup.config(show='*')




        #############___________PASSWORD CONFIRMATION ENTRY______________#############

    def on_enter4(self,e):
        self.conf.delete(0, "end")

    def on_leave4(self,e):
        if self.conf.get()=="":
            self.conf.insert(0, "Confirm Password")

    def show_password4(self):
        if self.conf.cget('show')=='*':
            self.conf.config(show='')
        else:
            self.conf.config(show='*')
                

    
    #############___________USERNAME ENTRY SIGN IN______________#############

    def on_enter5(self,e):
        self.user.delete(0, "end")

    def on_leave5(self,e):
        name=self.user.get()
        if name=="":
            self.user.insert(0, "Username")



    #############___________PASSWORD ENTRY SIGN IN______________#############

    def on_enter6(self,e):
        self.passw.delete(0, "end")

    def on_leave6(self,e):
        name=self.passw.get()
        if name=="":
            self.passw.insert(0, "Password")

    def show_password6(self):
        if self.passw.cget('show')=='*':
            self.passw.config(show='')
        else:
            self.passw.config(show='*')


root= Tk()


root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)
lgn=login_window(root)

lgn.usernameused()
root.protocol("WM_DELETE_WINDOW",lgn.callback)
root.mainloop()


class skaiciuokles():
    def __init__(self,langas):
        
        print(current_user)
        notebook_tab=ttk.Notebook(langas)
        notebook_tab.pack()

        frame1= Frame(notebook_tab, width=500, height=500)
        frame1.pack(fill="both", expand=1)

        frame2= Frame(notebook_tab, width=500, height=500)
        frame2.pack(fill="both", expand=1)
        self.frame2=frame2

        frame3=Frame(notebook_tab, width=500, height=500)
        frame3.pack(fill="both", expand=1)

        self.frame4=Frame(notebook_tab, width=500, height=500)
        self.frame4.pack(fill="both", expand=1)

        self.frame5=Frame(notebook_tab, width=500, height=500)
        self.frame5.pack(fill="both", expand=1)
        

        notebook_tab.add(frame1, text="KMI Skaičiuoklė")
        notebook_tab.add(frame2, text="KCAL Skaičiuoklė")
        notebook_tab.add(frame3, text="Kiek reikia išgerti vandens?")
        notebook_tab.add(self.frame4, text="Produkto maistinė vertė")
        notebook_tab.add(self.frame5, text="Mitybos planas")

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


        self.clicked=StringVar()
        self.clicked.set("Išskleisti")
        self.aktyvumo_pasirinkimai= ttk.Combobox(frame2, textvariable=self.clicked, state="readonly", width=35)
        
        self.aktyvumo_pasirinkimai["values"]= ("Labai mažas (nėra treniruočių, sėdimas darbas)", "Nedidelis (lengvos treniruotės, sėdimas darbas)", "Vidutinis (sunkios treniruotės, sėdimas darbas)", "Didelis (vidutinės treniruotės, aktyvus darbas)", "Labai didelis (sunkios treniruotės, aktyvus darbas)")
        self.aktyvumo_pasirinkimai.grid(sticky=W, column=0,columnspan=2, row=9)
        #Columnspan leidzia eiti per kelis stulpelius

        self.button3= tkinter.Button(frame2, text= "Dienos kalorijų norma", command=lambda: self.Zmogaus_info())
        self.button3.grid(column=0,row=12,sticky='E')

        ##################### FRAME 4 #########################################
        
        self.calories_1=0
        self.protein_1=0
        self.carbs_1=0
        self.fat_1=0
        self.sugars_1=0

        con2= sqlite3.connect("data.db")
        self.cur2= con2.cursor()
        statement= "SELECT produktas FROM produktai"
        self.cur2.execute(statement)
        result=(self.cur2.fetchall())

        self.my_list4=[r for r, in result]

        product=Label(self.frame4, text="Pasirinkite produktą")
        product.grid(column=0, row=0, sticky="w")

        self.product_entry = tk.StringVar()
        self.entry4 = tk.Entry(self.frame4, textvariable=self.product_entry)
        self.entry4.grid(column=0, row=1)

        self.food_results="Produkto vertė 100 g\n\nKalorijos: 0 kcal \nbaltymų: 0 g\nriebalų: 0 g\nangliavandenių: 0 g\niš kurių cukrų: 0 g"
        self.food=StringVar()
        self.food.set(self.food_results)
        food_label=Label(self.frame4, textvariable=self.food, justify=tk.LEFT)
        food_label.grid(column=3, row=1, rowspan=5, sticky="w")

        self.l4= tk.Listbox(self.frame4, height=10, width=39, relief="flat",
        bg="black",highlightcolor= "white")
        self.l4.grid(column=0, row=2)

        button4= Button(self.frame4, text= "Apskaičiuoti produkto vertę", command= self.button_clicked)
        button4.grid(column=0,row=4,sticky='E')

        self.l4.bind("<<ListboxSelect>>", self.my_upd4)
        self.product_entry.trace("w", self.get_data4)


        ##################### FRAME 5 #########################################
 
        con = sqlite3.connect('userdatatest.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS userplan(
                            weekday text,
                            diettime text,
                            product text, 
                            quantity number
                        )
                    ''')
        con.commit()

        self.calories1=0
        self.calories2=0
        self.calories3=0
        self.calories4=0
        self.calories5=0
        self.calories6=0
        self.calories7=0
        self.protein1=0
        self.protein2=0
        self.protein3=0
        self.protein4=0
        self.protein5=0
        self.protein6=0
        self.protein7=0
        self.carbs1=0
        self.carbs2=0
        self.carbs3=0
        self.carbs4=0
        self.carbs5=0
        self.carbs6=0
        self.carbs7=0
        self.fat1=0
        self.fat2=0
        self.fat3=0
        self.fat4=0
        self.fat5=0
        self.fat6=0
        self.fat7=0
        self.sugars1=0
        self.sugars2=0
        self.sugars3=0
        self.sugars4=0
        self.sugars5=0
        self.sugars6=0
        self.sugars7=0

        self.list_data = []
        self.selectionsql=[]



        self.clk= tk.StringVar()
        self.clk.set("Pirmadienis")
        drop2= ttk.Combobox(self.frame5, textvariable=self.clk, state="readonly", width=15)
        drop2["values"]=("Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis", "Šeštadienis", "Sekmadienis")
        drop2.grid(column=0, row=3, sticky="w")

  
        #-------------------
  

        self.clk2= tk.StringVar()
        self.clk2.set("Pusryčiai")
        drop1= ttk.Combobox(self.frame5, textvariable=self.clk2, state="readonly", width=15)
        drop1["values"]=("Pusryčiai", "Pietūs", "Vakarienė")
        drop1.grid(column=0, row=3, sticky="e")

        product=Label(self.frame5, text="Pasirinkite produktą")
        product.grid(column=0, row=0, sticky="w")

        self.content = tk.StringVar()
        self.entry5 = tk.Entry(self.frame5, textvariable=self.content)
        self.entry5.grid(column=0, row=1)

        #pasirinkimu listbox
        self.l5= tk.Listbox(self.frame5, height=10, width=39, relief="flat",
        bg="black", highlightcolor= "white")
        self.l5.grid(column=0, row=2)
        self.l5.bind("<<ListboxSelect>>", self.my_upd5)
        self.content.trace("w", self.get_data5)

        quantity_label=Label(self.frame5, text="Įveskite kiekį gramais")
        quantity_label.grid(column=0,row=4, sticky="w")

        self.content1 = tk.IntVar()
        quantity=tk.Entry(self.frame5,textvariable=self.content1)
        quantity.grid(column=0, row=5, sticky="w")

        #-------------LISTBOXES----------#

        self.monday_label=Label(self.frame5, text="PIRMADIENIS")
        self.monday_label.grid(column=1, row=1, padx=5)
        
        self.listbox1 = tk.Listbox(self.frame5, height=10, width=39)
        self.listbox1.grid(column=1, row=2, padx=3)

        self.monday_results=""
        self.results1=StringVar()
        self.results1.set(self.monday_results)
        results1_label=Label(self.frame5, textvariable=self.results1, justify=tk.LEFT)
        results1_label.grid(column=1, row=4, rowspan=5, sticky="w")

        tuesday_label=Label(self.frame5, text="ANTRADIENIS")
        tuesday_label.grid(column=2, row=1)
        self.listbox2 = tk.Listbox(self.frame5, width=39)
        self.listbox2.grid(column=2, row=2, padx=3)

        self.tuesday_results=""
        self.results2=StringVar()
        self.results2.set(self.tuesday_results)
        results2_label=Label(self.frame5, textvariable=self.results2, justify=tk.LEFT)
        results2_label.grid(column=2, row=4, rowspan=5, sticky="w")

        wednesday_label=Label(self.frame5, text="TREČIADIENIS")
        wednesday_label.grid(column=3, row=1)
        self.listbox3 = tk.Listbox(self.frame5, width=39)
        self.listbox3.grid(column=3, row=2, padx=3)

        self.wednesday_results=""
        self.results3=StringVar()
        self.results3.set(self.wednesday_results)
        results3_label=Label(self.frame5, textvariable=self.results3, justify=tk.LEFT)
        results3_label.grid(column=3, row=4, rowspan=5, sticky="w")

        thursday_label=Label(self.frame5, text="KETVIRTADIENIS")
        thursday_label.grid(column=0, row=9)
        self.listbox4 = tk.Listbox(self.frame5, width=39)
        self.listbox4.grid(column=0, row=10, padx=3)

        self.thursday_results=""
        self.results4=StringVar()
        self.results4.set(self.thursday_results)
        results4_label=Label(self.frame5, textvariable=self.results4, justify=tk.LEFT)
        results4_label.grid(column=0, row=12, rowspan=5, sticky="w")

        friday_label=Label(self.frame5, text="PENKTADIENIS")
        friday_label.grid(column=1, row=9)
        self.listbox5 = tk.Listbox(self.frame5, width=39)
        self.listbox5.grid(column=1, row=10, padx=3)

        self.friday_results=""
        self.results5=StringVar()
        self.results5.set(self.friday_results)
        results5_label=Label(self.frame5, textvariable=self.results5, justify=tk.LEFT)
        results5_label.grid(column=1, row=12, rowspan=5, sticky="w")

        saturday_label=Label(self.frame5, text="ŠEŠTADIENIS")
        saturday_label.grid(column=2, row=9)
        self.listbox6 = tk.Listbox(self.frame5, width=39)
        self.listbox6.grid(column=2, row=10, padx=3)

        self.saturday_results=""
        self.results6=StringVar()
        self.results6.set(self.saturday_results)
        results6_label=Label(self.frame5, textvariable=self.results6, justify=tk.LEFT)
        results6_label.grid(column=2, row=12, rowspan=5, sticky="w")

        sunday_label=Label(self.frame5, text="SEKMADIENIS")
        sunday_label.grid(column=3, row=9)
        self.listbox7 = tk.Listbox(self.frame5, width=39)
        self.listbox7.grid(column=3, row=10, padx=3)

        self.sunday_results=""
        self.results7=StringVar()
        self.results7.set(self.sunday_results)
        results7_label=Label(self.frame5, textvariable=self.results7, justify=tk.LEFT)
        results7_label.grid(column=3, row=12, rowspan=5, sticky="w")

        #-------------------BUTTONS-----------------#

        button = tk.Button(self.frame5, text="Pridėti", command=self.clicked5, width=10)
        button.grid(column=0, row=5, sticky="e")

        button_delete = tk.Button(self.frame5, text="Išvalyti viską", command=self.delete)
        button_delete.grid(column=0, row=6, sticky="w")

        button_delete_selected1 = tk.Button(self.frame5,text="Ištrinti pažymėtą", command=self.delete_selected1)
        button_delete_selected1.grid(column=1, row=3, sticky="w")

        button_delete_selected2 = tk.Button(self.frame5,text="Ištrinti pažymėtą", command=self.delete_selected2)
        button_delete_selected2.grid(column=2, row=3, sticky="w")

        button_delete_selected3 = tk.Button(self.frame5,text="Ištrinti pažymėtą", command=self.delete_selected3)
        button_delete_selected3.grid(column=3, row=3, sticky="w")

        button_delete_selected4 = tk.Button(self.frame5,text="Ištrinti pažymėtą", command=self.delete_selected4)
        button_delete_selected4.grid(column=0, row=11, sticky="w")

        button_delete_selected5 = tk.Button(self.frame5,text="Ištrinti pažymėtą", command=self.delete_selected5)
        button_delete_selected5.grid(column=1, row=11, sticky="w")

        button_delete_selected6 = tk.Button(self.frame5,text="Ištrinti pažymėtą", command=self.delete_selected6)
        button_delete_selected6.grid(column=2, row=11, sticky="w")

        button_delete_selected7 = tk.Button(self.frame5,text="Ištrinti pažymėtą", command=self.delete_selected7)
        button_delete_selected7.grid(column=3, row=11, sticky="w")

        bquit = tk.Button(self.frame5, text="Išsaugoti ir uždaryti", command=self.quit)
        bquit.grid(column=0, row=6, sticky="e")


        con2= sqlite3.connect("data.db")
        cur2= con2.cursor()
        statement= "SELECT produktas FROM produktai"
        cur2.execute(statement)
        result=(cur2.fetchall())

        self.my_list5=[p for p, in result]
        con2.commit()

        conn = sqlite3.connect('data.db')
        curr = conn.cursor()
        curr.execute('''CREATE TABLE IF NOT EXISTS userdietplan(
                    Planid NUMBER,
                    Username TEXT,
                    Weekday TEXT,
                    Meal TEXT,
                    Product TEXT,
                    Quantity NUMBER    
                )
            ''')

        conn = sqlite3.connect('data.db')
        curr = conn.cursor()
        curr.execute("SELECT distinct max(Planid) FROM userdietplan")
        rsl=curr.fetchone()[0]
        try:
            self.planid=rsl+1
        except:
            self.planid=1

    def button_clicked(self):

        try:

            self.cur2.execute("SELECT * FROM produktai WHERE produktas==:prod", {"prod":self.product_entry.get()})
            food_result=(self.cur2.fetchone())
            self.calories_1=food_result[2]
            self.protein_1=food_result[3]
            self.carbs_1=food_result[4]
            self.fat_1=food_result[5]
            self.sugars_1=food_result[6]
            food_results2="Produkto vertė 100 g\n\nKalorijos:  " + str(round(self.calories_1,1)) + " kcal \nbaltymų:        " + str(round(self.protein_1,1)) +  " g\nriebalų:        " + str(round(self.fat_1,1)) + " g\nangliavandenių: " + str(round(self.carbs_1,1)) + " g\niš kurių cukrų: " + str(round(self.sugars_1,1)) + " g"
            self.food.set(food_results2)

        except:

            messagebox.showerror("Invalid", "Pasirinkite produktą iš sąrašo!")
            self.food.set(self.food_results)

    def my_upd4(self, my_widget):

        my_w= my_widget.widget
        index= int (my_w.curselection()[0])
        value= my_w.get(index)
        self.product_entry.set(value)
        self.l4.delete(0, END)

    def get_data4(self, *args):
        search_str=self.entry4.get()
        self.l4.delete(0, END)
        for element in self.my_list4:
            if(re.match(search_str, element, re.IGNORECASE)):
                self.l4.insert(tk.END, element)



        ##################### MAIN FUNCTIONS FOR 1-3 FRAME #########################################

    
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

############################# FRAME 5 def
    def clicked5(self):

        con_clk = sqlite3.connect('data.db')
        cur_clk = con_clk.cursor()
        cur_clk.execute("SELECT * FROM produktai WHERE produktas==:product", {"product":self.content.get()})
        sqlresult=cur_clk.fetchone()

        if self.clk.get()=="Pirmadienis":
            self.listbox1.insert(tk.END, self.clk2.get().upper() + ": "+self.content.get()+ ", * "+str(self.content1.get()) + "g")
            
            self.calories1+=((self.content1.get()/100)*sqlresult[2])
            self.protein1+=((self.content1.get()/100)*sqlresult[3])
            self.carbs1+=((self.content1.get()/100)*sqlresult[4])
            self.fat1+=((self.content1.get()/100)*sqlresult[5])
            self.sugars1+=((self.content1.get()/100)*sqlresult[6])

            self.monday_results="Viso kalorijų:  " + str(round(self.calories1,1)) + " kcal \nbaltymų:        " + str(round(self.protein1,1)) +  " g\nriebalų:        " + str(round(self.fat1,1)) + " g\nangliavandenių: " + str(round(self.carbs1,1)) + " g\niš kurių cukrų: " + str(round(self.sugars1,1)) + " g"

        elif self.clk.get()=="Antradienis":
            self.listbox2.insert(tk.END, self.clk2.get().upper() + ": "+self.content.get()+ ", * "+str(self.content1.get()) + "g")
            
            self.calories2+=((self.content1.get()/100)*sqlresult[2])
            self.protein2+=((self.content1.get()/100)*sqlresult[3])
            self.carbs2+=((self.content1.get()/100)*sqlresult[4])
            self.fat2+=((self.content1.get()/100)*sqlresult[5])
            self.sugars2+=((self.content1.get()/100)*sqlresult[6])
            self.tuesday_results="Viso kalorijų:  " + str(round(self.calories2,1)) + " kcal \nbaltymų:        " + str(round(self.protein2,1)) +  " g\nriebalų:        " + str(round(self.fat2,1)) + " g\nangliavandenių: " + str(round(self.carbs2,1)) + " g\niš kurių cukrų: " + str(round(self.sugars2,1)) + " g"
            
        elif self.clk.get()=="Trečiadienis":
            self.listbox3.insert(tk.END, self.clk2.get().upper() + ": "+self.content.get()+ ", * "+str(self.content1.get()) + "g")
            
            self.calories3+=((self.content1.get()/100)*sqlresult[2])
            self.protein3+=((self.content1.get()/100)*sqlresult[3])
            self.carbs3+=((self.content1.get()/100)*sqlresult[4])
            self.fat3+=((self.content1.get()/100)*sqlresult[5])
            self.sugars3+=((self.content1.get()/100)*sqlresult[6])
            self.wednesday_results="Viso kalorijų:  " + str(round(self.calories3,1)) + " kcal \nbaltymų:        " + str(round(self.protein3,1)) +  " g\nriebalų:        " + str(round(self.fat3,1)) + " g\nangliavandenių: " + str(round(self.carbs3,1)) + " g\niš kurių cukrų: " + str(round(self.sugars3,1)) + " g"
            
        elif self.clk.get()=="Ketvirtadienis":
            self.listbox4.insert(tk.END, self.clk2.get().upper() + ": "+self.content.get()+ ", * "+str(self.content1.get()) + "g")


            self.calories4+=((self.content1.get()/100)*sqlresult[2])
            self.protein4+=((self.content1.get()/100)*sqlresult[3])
            self.carbs4+=((self.content1.get()/100)*sqlresult[4])
            self.fat4+=((self.content1.get()/100)*sqlresult[5])
            self.sugars4+=((self.content1.get()/100)*sqlresult[6])
            self.thursday_results="Viso kalorijų:  " + str(round(self.calories4,1)) + " kcal \nbaltymų:        " + str(round(self.protein4,1)) +  " g\nriebalų:        " + str(round(self.fat4,1)) + " g\nangliavandenių: " + str(round(self.carbs4,1)) + " g\niš kurių cukrų: " + str(round(self.sugars4,1)) + " g"


        elif self.clk.get()=="Penktadienis":
            self.listbox5.insert(tk.END, self.clk2.get().upper() + ": "+self.content.get()+ ", * "+str(self.content1.get()) + "g")

            self.calories5+=((self.content1.get()/100)*sqlresult[2])
            self.protein5+=((self.content1.get()/100)*sqlresult[3])
            self.carbs5+=((self.content1.get()/100)*sqlresult[4])
            self.fat5+=((self.content1.get()/100)*sqlresult[5])
            self.sugars5+=((self.content1.get()/100)*sqlresult[6])
            self.friday_results="Viso kalorijų:  " + str(round(self.calories5,1)) + " kcal \nbaltymų:        " + str(round(self.protein5,1)) +  " g\nriebalų:        " + str(round(self.fat5,1)) + " g\nangliavandenių: " + str(round(self.carbs5,1)) + " g\niš kurių cukrų: " + str(round(self.sugars5,1)) + " g"

        elif self.clk.get()=="Šeštadienis":
            self.listbox6.insert(tk.END, self.clk2.get().upper() + ": "+self.content.get()+ ", * "+str(self.content1.get()) + "g")

            self.calories6+=((self.content1.get()/100)*sqlresult[2])
            self.protein6+=((self.content1.get()/100)*sqlresult[3])
            self.carbs6+=((self.content1.get()/100)*sqlresult[4])
            self.fat6+=((self.content1.get()/100)*sqlresult[5])
            self.sugars6+=((self.content1.get()/100)*sqlresult[6])
            self.saturday_results="Viso kalorijų:  " + str(round(self.calories6,1)) + " kcal \nbaltymų:        " + str(round(self.protein6,1)) +  " g\nriebalų:        " + str(round(self.fat6,1)) + " g\nangliavandenių: " + str(round(self.carbs6,1)) + " g\niš kurių cukrų: " + str(round(self.sugars6,1)) + " g"
        
        elif self.clk.get()=="Sekmadienis":
            self.listbox7.insert(tk.END, self.clk2.get().upper() + ": "+self.content.get()+ ", * "+str(self.content1.get()) + "g")

            self.calories7+=((self.content1.get()/100)*sqlresult[2])
            self.protein7+=((self.content1.get()/100)*sqlresult[3])
            self.carbs7+=((self.content1.get()/100)*sqlresult[4])
            self.fat7+=((self.content1.get()/100)*sqlresult[5])
            self.sugars7+=((self.content1.get()/100)*sqlresult[6])
            self.sunday_results="Viso kalorijų:  " + str(round(self.calories7,1)) + " kcal \nbaltymų:        " + str(round(self.protein7,1)) +  " g\nriebalų:        " + str(round(self.fat7,1)) + " g\nangliavandenių: " + str(round(self.carbs7,1)) + " g\niš kurių cukrų: " + str(round(self.sugars7,1)) + " g"
        
        self.selectionsdic={"planid":self.planid, "user":current_user, "weekday":self.clk.get(),"meal":self.clk2.get(),"product":self.content.get(), "quantity":self.content1.get()}
        self.selectionsql.append(self.selectionsdic)
        self.list_data.append(self.content.get())
        self.results1.set(self.monday_results)
        self.results2.set(self.tuesday_results)
        self.results3.set(self.wednesday_results)
        self.results4.set(self.thursday_results)
        self.results5.set(self.friday_results)
        self.results6.set(self.saturday_results)
        self.results7.set(self.sunday_results)

        print(self.selectionsql)
        print(self.selectionsdic)
        con_clk.commit()
    def delete(self):
        self.listbox1.delete(0, tk.END)
        self.listbox2.delete(0, tk.END)
        self.listbox3.delete(0, tk.END)
        self.listbox4.delete(0, tk.END)
        self.listbox5.delete(0, tk.END)
        self.listbox6.delete(0, tk.END)
        self.listbox7.delete(0, tk.END)
        self.list_data = []

        self.calories1=0
        self.calories2=0
        self.calories3=0
        self.calories4=0
        self.calories5=0
        self.calories6=0
        self.calories7=0
        self.protein1=0
        self.protein2=0
        self.protein3=0
        self.protein4=0
        self.protein5=0
        self.protein6=0
        self.protein7=0
        self.carbs1=0
        self.carbs2=0
        self.carbs3=0
        self.carbs4=0
        self.carbs5=0
        self.carbs6=0
        self.carbs7=0
        self.fat1=0
        self.fat2=0
        self.fat3=0
        self.fat4=0
        self.fat5=0
        self.fat6=0
        self.fat7=0
        self.sugars1=0
        self.sugars2=0
        self.sugars3=0
        self.sugars4=0
        self.sugars5=0
        self.sugars6=0
        self.sugars7=0

        self.monday_results=""
        self.tuesday_results=""
        self.wednesday_results=""
        self.thursday_results=""
        self.friday_results=""
        self.saturday_results=""
        self.sunday_results=""


        self.results1.set(self.monday_results)
        self.results2.set(self.tuesday_results)
        self.results3.set(self.wednesday_results)
        self.results4.set(self.thursday_results)
        self.results5.set(self.friday_results)
        self.results6.set(self.saturday_results)
        self.results7.set(self.sunday_results)

        self.selectionsql.clear()
        self.selectionsdic.clear

    def delete_selected1(self):
        try:

            selected1= self.listbox1.get(self.listbox1.curselection())
            self.listbox1.delete(tk.ANCHOR)
            
            p=re.search('(.*): ', selected1)
            if p:
                meal_name = p.group(1)

            m=re.search(': (.*), *', selected1)
            if m:
                product_name = m.group(1)

            n=re.search(',* (\d*)g', selected1)
            if n:
                svoris = int(n.group(1))

            con5= sqlite3.connect("data.db")
            cur5= con5.cursor()
            cur5.execute("SELECT * FROM produktai WHERE produktas==:prd", {"prd":product_name})
            result5=(cur5.fetchone())

            self.calories1-=((svoris/100)*result5[2])
            self.protein1-=((svoris/100)*result5[3])
            self.carbs1-=((svoris/100)*result5[4])
            self.fat1-=((svoris/100)*result5[5])
            self.sugars1-=((svoris/100)*result5[6])
            self.monday_results="Viso kalorijų:  " + str(round(self.calories1,1)) + " kcal \nbaltymų:        " + str(round(self.protein1,1)) +  " g\nriebalų:        " + str(round(self.fat1,1)) + " g\nangliavandenių: " + str(round(self.carbs1,1)) + " g\niš kurių cukrų: " + str(round(self.sugars1,1)) + " g"
            con5.commit()
            self.results1.set(self.monday_results)

            for i in range(len(self.selectionsql)):
                if self.selectionsql[i]["weekday"]=="Pirmadienis" and self.selectionsql[i]["meal"]==meal_name.lower().capitalize() and self.selectionsql[i]["product"]==product_name and self.selectionsql[i]["quantity"]==svoris:
                    del self.selectionsql[i]
                    break
                

        except:
            pass

    def delete_selected2(self):
        try:
            selected1= self.listbox2.get(self.listbox2.curselection())
            self.listbox2.delete(tk.ANCHOR)

            p=re.search('(.*): ', selected1)
            if p:
                meal_name = p.group(1)

            m=re.search(': (.*), *', selected1)
            if m:
                product_name = m.group(1)
            n=re.search(',* (\d*)g', selected1)
            if n:
                svoris = int(n.group(1))

            con5= sqlite3.connect("data.db")
            cur5= con5.cursor()
            cur5.execute("SELECT * FROM produktai WHERE produktas==:prd", {"prd":product_name})
            result5=(cur5.fetchone())

            self.calories2-=((svoris/100)*result5[2])
            self.protein2-=((svoris/100)*result5[3])
            self.carbs2-=((svoris/100)*result5[4])
            self.fat2-=((svoris/100)*result5[5])
            self.sugars2-=((svoris/100)*result5[6])
            self.tuesday_results="Viso kalorijų:  " + str(round(self.calories2,1)) + " kcal \nbaltymų:        " + str(round(self.protein2,1)) +  " g\nriebalų:        " + str(round(self.fat2,1)) + " g\nangliavandenių: " + str(round(self.carbs2,1)) + " g\niš kurių cukrų: " + str(round(self.sugars2,1)) + " g"
            con5.commit()
            self.results2.set(self.tuesday_results)

            for i in range(len(self.selectionsql)):
                if self.selectionsql[i]["weekday"]=="Antradienis" and self.selectionsql[i]["meal"]==meal_name.lower().capitalize() and self.selectionsql[i]["product"]==product_name and self.selectionsql[i]["quantity"]==svoris:
                    del self.selectionsql[i]
                    break
        except:
            pass

    def delete_selected3(self):
        try:
            selected1= self.listbox3.get(self.listbox3.curselection())
            self.listbox3.delete(tk.ANCHOR)

            p=re.search('(.*): ', selected1)
            if p:
                meal_name = p.group(1)

            m=re.search(': (.*), *', selected1)
            if m:
                product_name = m.group(1)
            n=re.search(',* (\d*)g', selected1)
            if n:
                svoris = int(n.group(1))

            con5= sqlite3.connect("data.db")
            cur5= con5.cursor()
            cur5.execute("SELECT * FROM produktai WHERE produktas==:prd", {"prd":product_name})
            result5=(cur5.fetchone())

            self.calories3-=((svoris/100)*result5[2])
            self.protein3-=((svoris/100)*result5[3])
            self.carbs3-=((svoris/100)*result5[4])
            self.fat3-=((svoris/100)*result5[5])
            self.sugars3-=((svoris/100)*result5[6])
            self.wednesday_results="Viso kalorijų:  " + str(round(self.calories3,1)) + " kcal \nbaltymų:        " + str(round(self.protein3,1)) +  " g\nriebalų:        " + str(round(self.fat3,1)) + " g\nangliavandenių: " + str(round(self.carbs3,1)) + " g\niš kurių cukrų: " + str(round(self.sugars3,1)) + " g"
            con5.commit()
            self.results3.set(self.wednesday_results)

            for i in range(len(self.selectionsql)):
                if self.selectionsql[i]["weekday"]=="Trečiadienis" and self.selectionsql[i]["meal"]==meal_name.lower().capitalize() and self.selectionsql[i]["product"]==product_name and self.selectionsql[i]["quantity"]==svoris:
                    del self.selectionsql[i]
                    break
        except:
            pass
       
    def delete_selected4(self):
        try:
            selected1= self.listbox4.get(self.listbox4.curselection())
            self.listbox4.delete(tk.ANCHOR)

            p=re.search('(.*): ', selected1)
            if p:
                meal_name = p.group(1)

            m=re.search(': (.*), *', selected1)
            if m:
                product_name = m.group(1)
            n=re.search(',* (\d*)g', selected1)
            if n:
                svoris = int(n.group(1))

            con5= sqlite3.connect("data.db")
            cur5= con5.cursor()
            cur5.execute("SELECT * FROM produktai WHERE produktas==:prd", {"prd":product_name})
            result5=(cur5.fetchone())

            self.calories4-=((svoris/100)*result5[2])
            self.protein4-=((svoris/100)*result5[3])
            self.carbs4-=((svoris/100)*result5[4])
            self.fat4-=((svoris/100)*result5[5])
            self.sugars4-=((svoris/100)*result5[6])
            self.thursday_results="Viso kalorijų:  " + str(round(self.calories4,1)) + " kcal \nbaltymų:        " + str(round(self.protein4,1)) +  " g\nriebalų:        " + str(round(self.fat4,1)) + " g\nangliavandenių: " + str(round(self.carbs4,1)) + " g\niš kurių cukrų: " + str(round(self.sugars4,1)) + " g"
            con5.commit()
            self.results4.set(self.thursday_results)

            for i in range(len(self.selectionsql)):
                if self.selectionsql[i]["weekday"]=="Ketvirtadienis" and self.selectionsql[i]["meal"]==meal_name.lower().capitalize() and self.selectionsql[i]["product"]==product_name and self.selectionsql[i]["quantity"]==svoris:
                    del self.selectionsql[i]
                    break
        except:
            pass

    def delete_selected5(self):
        try:
            selected1= self.listbox5.get(self.listbox5.curselection())
            self.listbox5.delete(tk.ANCHOR)

            p=re.search('(.*): ', selected1)
            if p:
                meal_name = p.group(1)

            m=re.search(': (.*), *', selected1)
            if m:
                product_name = m.group(1)
            n=re.search(',* (\d*)g', selected1)
            if n:
                svoris = int(n.group(1))

            con5= sqlite3.connect("data.db")
            cur5= con5.cursor()
            cur5.execute("SELECT * FROM produktai WHERE produktas==:prd", {"prd":product_name})
            result5=(cur5.fetchone())

            self.calories5-=((svoris/100)*result5[2])
            self.protein5-=((svoris/100)*result5[3])
            self.carbs5-=((svoris/100)*result5[4])
            self.fat5-=((svoris/100)*result5[5])
            self.sugars5-=((svoris/100)*result5[6])
            self.friday_results="Viso kalorijų:  " + str(round(self.calories5,1)) + " kcal \nbaltymų:        " + str(round(self.protein5,1)) +  " g\nriebalų:        " + str(round(self.fat5,1)) + " g\nangliavandenių: " + str(round(self.carbs5,1)) + " g\niš kurių cukrų: " + str(round(self.sugars5,1)) + " g"
            con5.commit()
            self.results5.set(self.friday_results)

            for i in range(len(self.selectionsql)):
                if self.selectionsql[i]["weekday"]=="Penktadienis" and self.selectionsql[i]["meal"]==meal_name.lower().capitalize() and self.selectionsql[i]["product"]==product_name and self.selectionsql[i]["quantity"]==svoris:
                    del self.selectionsql[i]
                    break
        except:
            pass

    def delete_selected6(self):
        try:
            selected1= self.listbox6.get(self.listbox6.curselection())
            self.listbox6.delete(tk.ANCHOR)

            p=re.search('(.*): ', selected1)
            if p:
                meal_name = p.group(1)

            m=re.search(': (.*), *', selected1)
            if m:
                product_name = m.group(1)
            n=re.search(',* (\d*)g', selected1)
            if n:
                svoris = int(n.group(1))

            con5= sqlite3.connect("data.db")
            cur5= con5.cursor()
            cur5.execute("SELECT * FROM produktai WHERE produktas==:prd", {"prd":product_name})
            result5=(cur5.fetchone())

            self.calories6-=((svoris/100)*result5[2])
            self.protein6-=((svoris/100)*result5[3])
            self.carbs6-=((svoris/100)*result5[4])
            self.fat6-=((svoris/100)*result5[5])
            self.sugars6-=((svoris/100)*result5[6])
            self.saturday_results="Viso kalorijų:  " + str(round(self.calories6,1)) + " kcal \nbaltymų:        " + str(round(self.protein6,1)) +  " g\nriebalų:        " + str(round(self.fat6,1)) + " g\nangliavandenių: " + str(round(self.carbs6,1)) + " g\niš kurių cukrų: " + str(round(self.sugars6,1)) + " g"
            con5.commit()
            self.results6.set(self.saturday_results)

            for i in range(len(self.selectionsql)):
                if self.selectionsql[i]["weekday"]=="Šeštadienis" and self.selectionsql[i]["meal"]==meal_name.lower().capitalize() and self.selectionsql[i]["product"]==product_name and self.selectionsql[i]["quantity"]==svoris:
                    del self.selectionsql[i]
                    break
        except:
            pass

    def delete_selected7(self):
        try:
            selected1= self.listbox7.get(self.listbox7.curselection())
            self.listbox7.delete(tk.ANCHOR)

            p=re.search('(.*): ', selected1)
            if p:
                meal_name = p.group(1)

            m=re.search(': (.*), *', selected1)
            if m:
                product_name = m.group(1)
            n=re.search(',* (\d*)g', selected1)
            if n:
                svoris = int(n.group(1))

            con5= sqlite3.connect("data.db")
            cur5= con5.cursor()
            cur5.execute("SELECT * FROM produktai WHERE produktas==:prd", {"prd":product_name})
            result5=(cur5.fetchone())

            self.calories7-=((svoris/100)*result5[2])
            self.protein7-=((svoris/100)*result5[3])
            self.carbs7-=((svoris/100)*result5[4])
            self.fat7-=((svoris/100)*result5[5])
            self.sugars7-=((svoris/100)*result5[6])
            self.sunday_results="Viso kalorijų:  " + str(round(self.calories7,1)) + " kcal \nbaltymų:        " + str(round(self.protein7,1)) +  " g\nriebalų:        " + str(round(self.fat7,1)) + " g\nangliavandenių: " + str(round(self.carbs7,1)) + " g\niš kurių cukrų: " + str(round(self.sugars7,1)) + " g"
            con5.commit()
            self.results7.set(self.sunday_results)

            for i in range(len(self.selectionsql)):
                if self.selectionsql[i]["weekday"]=="Sekmadienis" and self.selectionsql[i]["meal"]==meal_name.lower().capitalize() and self.selectionsql[i]["product"]==product_name and self.selectionsql[i]["quantity"]==svoris:
                    del self.selectionsql[i]
                    break
        except:
            pass

    def quit(self):
        conn = sqlite3.connect('data.db')
        curr = conn.cursor()

        for i in range(len(self.selectionsql)):
            curr.execute("INSERT INTO userdietplan VALUES (:planid, :user, :weekday, :meal, :product, :quantity)", {
                'planid': self.planid,
                'user': current_user,
                'weekday': self.selectionsql[i]["weekday"],
                'meal': self.selectionsql[i]["meal"],
                'product': self.selectionsql[i]["product"],
                'quantity': self.selectionsql[i]["quantity"]})

        conn.commit()
        self.make_csv()
        # self.email()
        exit()

    def make_csv(self):
        con = sqlite3.connect('data.db')
        c = con.cursor()
        c.execute("SELECT u.Username as Slapyvardis, u. Weekday as Savaitės_Diena, u. Meal as Valgio_metas, u.Product as Produktas_Patiekalas, u.Quantity as Kiekis, round((cast(u.Quantity as real)/100* (p.baltymai)),1) as Kalorijos, round(cast(u.Quantity as real)/100* (p.baltymai),1) as Baltymai, round(cast(u.Quantity as real)/100* (p.riebalai),1) as Riebalai, round(cast(u.Quantity as real)/100* (p.angliavandeniai),1) as Angliavandeniai, round(cast(u.Quantity as real)/100* (p.cukrus),1) as Cukrus FROM userdietplan u LEFT JOIN produktai p on u.Product=p.produktas WHERE u.Planid==:pln", {"pln":self.planid})


        with open ('mitybosplanas.csv', 'w', newline='') as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow([i[0] for i in c.description])
            writer.writerows(c)
        con.close()
            # men=1
            # for r in self.selectionsql:
            #     # r.insert(0,men)
            #     writer.writerow(r)
            #     # men+=1

    def my_upd5(self, my_widget):
        my_w= my_widget.widget
        index= int (my_w.curselection()[0])
        value= my_w.get(index)
        self.content.set(value)
        self.l5.delete(0, END)

    def get_data5(self, *args):
        search_str=self.entry5.get()
        self.l5.delete(0, END)
        for element in self.my_list5:
            if(re.match(search_str, element, re.IGNORECASE)):
                self.l5.insert(tk.END, element)


    def email(self):

        emailfrom = "mindpythonas@gmail.com"
        emailto = "mindpythonas@gmail.com"
        fileToSend = "mitybosplanas.csv"
        username = "mindpythonas@gmail.com"
        password = kodas

        msg = MIMEMultipart()
        msg["From"] = emailfrom
        msg["To"] = emailto
        msg["Subject"] = "Sveiki. Siunčiame Jums mitybos planą"
        msg.preamble = "Sveiki. Siunčiame Jums mitybos planą"

        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)

        maintype == "text"
        fp = open(fileToSend)

        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()

        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)

        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
        msg.attach(attachment)

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        server.sendmail(emailfrom, emailto, msg.as_string().encode('utf-8'))
        server.quit()   

root1= Tk()
langas1=skaiciuokles(root1)
root1.title("Skaičiuoklė")
root1.geometry("1600x2560")
root1.mainloop()