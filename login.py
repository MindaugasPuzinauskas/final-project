import email
from tkinter import *
from tkinter import messagebox
import sqlite3
import re
from datetime import datetime
from PIL import ImageTk, Image


con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    Username TEXT PRIMARY KEY,
                    Email TEXT NOT NULL UNIQUE,
                    Password TEXT,
                    DateCreated TEXT
                    
                )
            ''')
con.commit()


root= Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username= user.get()
    password=passw.get()

    con = sqlite3.connect('userdata.db')
    c = con.cursor()
    c.execute("Select * from record where username==:name", {"name":username})

    if username=="Username":
        messagebox.showerror("Ivnalid", "Username can not be empty!")
    else:

        if c.fetchone()==None:
            messagebox.showinfo("Sign up", "Username doesn't exist")
        else:
            c.execute("Select * from record where username==:name and password==:pwd", {"name":username, "pwd":password})
            if c.fetchone()==None:
                messagebox.showerror("Invalid", "Invalid username or password!")
            else:  
                messagebox.showinfo("Sign up", "Signed In")
    con.commit()


############################   SIGN UP FORM #########################

def signup_command():
    window=Toplevel(root)

    window.title("Sign Up")
    window.geometry("925x500+300+200")
    window.configure(bg= "#fff")
    window.resizable(False, False)

    def signup():
        username=user.get()
        password=passw.get()
        confim_passw=conf.get()
        email= e_email.get()


        current_datetime=datetime.now().strftime("%B %d, %Y %I:%M%p")
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        con = sqlite3.connect('userdata.db')
        acur = con.cursor()
        acur.execute("Select * from record where username==:name;", {"name":username})
        if username=="Username":
            messagebox.showerror("Invalid", "Username can not be empty!")
        elif email=="Email":
            messagebox.showerror("Invalid", "Email can not be empty!")
        elif not re.fullmatch(email_pattern,email):
            messagebox.showerror("Invalid", "Please input valid E-mail!")
        elif password=="Password":
            messagebox.showerror("Invalid", "Password can not be empty!")
        elif len(password)<6:
            messagebox.showerror("Invalid", "Password must contain at least 6 characters!")
        else:
            
            if acur.fetchone()!=None:
                messagebox.showerror("Invalid", "Selected username already exists!")
            else:
                acur.execute("Select * from record where Email==:email;", {"email":email})
                if acur.fetchone()!=None:
                    messagebox.showerror("Invalid", "Selected email already exists!")
                else:
                    if password==confim_passw:
                        acur.execute("INSERT INTO record VALUES (:name, :email, :password, :datetime)", {
                            'name': user.get(),
                            'password': passw.get(),
                            'email': e_email.get(),
                            'datetime':current_datetime})

                        messagebox.showinfo("Signup", "Sucessfully sign up")
                        window.destroy()
                    else:
                        messagebox.showerror("Invalid", "Both Password should match!")
            
    
        con.commit()

    def sign():
        window.destroy()


    img=PhotoImage(file="signup.png")
    Label(window, image=img, border=0, bg="white").place(x=0, y=0)

    frame=Frame(window, width=450, height=570, bg="#fff")
    frame.place(x=480, y=50)

    heading=Label(frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23,"bold"))
    heading.place(x=100, y=5)

#############___________USERNAME ENTRY______________#############

    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        if user.get()=="":
            user.insert(0, "Username")


    user=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    username_icon= Image.open('name-icon.png')
    photo= ImageTk.PhotoImage(username_icon)
    username_icon_label= Label(frame, image=photo, bg='white')
    username_icon_label.image=photo
    username_icon_label.place(x=0, y=75)

#############___________EMAIL ENTRY______________#############

    def on_enter(e):
        e_email.delete(0, "end")

    def on_leave(e):
        if e_email.get()=="":
            e_email.insert(0, "Email")
                

    e_email=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    e_email.place(x=30, y=150)
    e_email.insert(0, "Email")
    e_email.bind("<FocusIn>", on_enter)
    e_email.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    email_icon= Image.open('email-icon.png')
    photo= ImageTk.PhotoImage(email_icon)
    email_icon_label= Label(frame, image=photo, bg='white')
    email_icon_label.image=photo
    email_icon_label.place(x=0, y=148)


#############___________PASSWORD ENTRY______________#############
    
    def on_enter(e):
        passw.delete(0, "end")

    def on_leave(e):
        if passw.get()=="":
            passw.insert(0, "Password")

    def show_password():
        if passw.cget('show')=='*':
            passw.config(show='')
        else:
            passw.config(show='*')


    passw=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11), show="*")
    passw.place(x=30, y=220)
    passw.insert(0, "Password")
    passw.bind("<FocusIn>", on_enter)
    passw.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=317)

    check_button= Checkbutton(frame, text="Show Password", command=show_password)
    check_button.place(x=30, y=250)

    pass_icon= Image.open('pass-icon.png')
    photo= ImageTk.PhotoImage(pass_icon)
    pass_icon_label= Label(frame, image=photo, bg='white')
    pass_icon_label.image=photo
    pass_icon_label.place(x=0, y=215)

    #############___________PASSWORD CONFIRMATION ENTRY______________#############

    def on_enter(e):
        conf.delete(0, "end")

    def on_leave(e):
        if conf.get()=="":
            conf.insert(0, "Confirm Password")

    def show_password():
        if conf.cget('show')=='*':
            conf.config(show='')
        else:
            conf.config(show='*')
            

    conf=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11), show="*")
    conf.place(x=30, y=290)
    conf.insert(0, "Confirm Password")
    conf.bind("<FocusIn>", on_enter)
    conf.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    check_button1= Checkbutton(frame, text="Show Password", command=show_password)
    check_button1.place(x=30, y=320)

    pass_icon= Image.open('pass-icon.png')
    photo= ImageTk.PhotoImage(pass_icon)
    pass_icon_label= Label(frame, image=photo, bg='white')
    pass_icon_label.image=photo
    pass_icon_label.place(x=0, y=285)


#############___________SIGN UP BUTTON______________#############

    Button(frame, width=39, pady=7, text="Sign Up", fg="#57a1f8", bg="#57a1f8", border=0, command=signup).place(x=35, y=350)
    label=Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
    label.place(x=90, y=410)

    signin=Button(frame, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign)
    signin.place(x=200, y=410)



    window.mainloop()


img=PhotoImage(file="login.png")
Label(root, image=img, border=0, bg="white").place(x=50, y=90)

frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text="Sign In", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

#############___________USERNAME ENTRY SIGN IN______________#############

def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0, "Username")

user= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

username_icon= Image.open('name-icon.png')
photo= ImageTk.PhotoImage(username_icon)
username_icon_label= Label(frame, image=photo, bg='white')
username_icon_label.image=photo
username_icon_label.place(x=0, y=75)

#############___________PASSWORD ENTRY SIGN IN______________#############

def on_enter(e):
    passw.delete(0, "end")

def on_leave(e):
    name=passw.get()
    if name=="":
        passw.insert(0, "Password")

def show_password():
    if passw.cget('show')=='*':
        passw.config(show='')
    else:
        passw.config(show='*')

passw= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11), show="*")
passw.place(x=30, y=150)
passw.insert(0, "Password")
passw.bind("<FocusIn>", on_enter)
passw.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

check_button= Checkbutton(frame, text="Show Password", command=show_password)
check_button.place(x=30, y=180)

pass_icon= Image.open('pass-icon.png')
photo= ImageTk.PhotoImage(pass_icon)
pass_icon_label= Label(frame, image=photo, bg='white')
pass_icon_label.image=photo
pass_icon_label.place(x=0, y=150)

#############___________SIGN IN BUTTON______________#############

Button(frame, width=30, pady=7, text="Sign in", fg="#57a1f8", bg="#57a1f8", border=0, command=signin).place(x=35, y=215)
label= Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75,y=270)

sign_up= Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()