from curses import window
import imp
from tkinter import *
from tkinter import messagebox
import ast
import sqlite3

con = sqlite3.connect('testuserdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    username text PRIMARY KEY, 
                    password text
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

    con = sqlite3.connect('testuserdata.db')
    c = con.cursor()
    c.execute("Select * from record where username==:name", {"name":username})
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

        con = sqlite3.connect('testuserdata.db')
        acur = con.cursor()

        acur.execute("Select * from record where username==:name", {"name":username})
        if acur.fetchone()!=None:
            messagebox.showerror("Invalid", "Selected user name already exists!")
        else:
            if password==confim_passw:
                acur.execute("INSERT INTO record VALUES (:name, :password)", {
                    'name': user.get(),
                    'password': passw.get()})
                messagebox.showinfo("Signup", "Sucessfully sign up")
                window.destroy()
            else:
                messagebox.showerror("Invalid", "Both Password should match!")
            
    
        con.commit()

    def sign():
        window.destroy()


    img=PhotoImage(file="login.png")
    Label(window, image=img, border=0, bg="white").place(x=50, y=90)

    frame=Frame(window, width=350, height=390, bg="#fff")
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

#############___________PASWORD ENTRY______________#############



    def on_enter(e):
        passw.delete(0, "end")

    def on_leave(e):
        if passw.get()=="":
            passw.insert(0, "Password")



    passw=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    passw.place(x=30, y=150)
    passw.insert(0, "Password")
    passw.bind("<FocusIn>", on_enter)
    passw.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    #############___________CONFIRMATION ENTRY______________#############

    def on_enter(e):
        conf.delete(0, "end")

    def on_leave(e):
        if conf.get()=="":
            conf.insert(0, "Confirm Password")



    conf=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
    conf.place(x=30, y=220)
    conf.insert(0, "Confirm Password")
    conf.bind("<FocusIn>", on_enter)
    conf.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

#############___________SIGN UP BUTTON______________#############

    Button(frame, width=39, pady=7, text="Sign Up", fg="#57a1f8", bg="#57a1f8", border=0, command=signup).place(x=35, y=280)
    label=Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
    label.place(x=90, y=340)

    signin=Button(frame, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign)
    signin.place(x=200, y=340)



    window.mainloop()


img=PhotoImage(file="login.png")
Label(root, image=img, border=0, bg="white").place(x=50, y=90)

frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text="Sign In", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

#############___________USERNAME ENTRY______________#############

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

#############___________PASSWORD ENTRY______________#############

def on_enter(e):
    passw.delete(0, "end")

def on_leave(e):
    name=passw.get()
    if name=="":
        passw.insert(0, "Password")

passw= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
passw.place(x=30, y=150)
passw.insert(0, "Password")
passw.bind("<FocusIn>", on_enter)
passw.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

#############___________SIGN IN BUTTON______________#############

Button(frame, width=39, pady=7, text="Sign in", fg="#57a1f8", bg="#57a1f8", border=0, command=signin).place(x=35, y=204)
label= Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75,y=270)

sign_up= Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()