import sqlite3 as sql
import tkinter as tk
import re
from tkinter import ACTIVE, ANCHOR, END, Button, Label


my_w= tk.Tk()
my_w.geometry("600x600")
font1= ("Times", 18, "bold")


con= sql.connect("data.db")
cur= con.cursor()
statement= "SELECT produktas FROM produktai"
cur.execute(statement)
result=(cur.fetchall())



my_list=[r for r, in result]

l0=tk.Label(text="Pasirinkite produktą", font=font1)
l0.grid(row=0, column=1)

def my_upd(my_widget):
    my_w= my_widget.widget
    index= int (my_w.curselection()[0])
    value= my_w.get(index)
    e1_str.set(value)
    l1.delete(0, END)

def my_down(my_widget):
    l1.focus()
    l1.selection_set(0)

e1_str= tk.StringVar()
e1= tk.Entry(my_w, textvariable=e1_str, font=font1)
e1.grid(row=1, column=1, padx=50, pady=0)

l1= tk.Listbox(my_w, height=15, width=70, font=font1, relief="flat",
    bg="black", highlightcolor= "white")
l1.grid(row=2, column=1)

def get_data(*args):
    search_str=e1.get()
    l1.delete(0, END)
    for element in my_list:
        if(re.match(search_str, element, re.IGNORECASE)):
            l1.insert(tk.END, element)

# def select():
#     my_label.config(text= result.get(ANCHOR))

# my_button2= Button(my_w, text='Select', command= select)
# my_button2.grid(row=4, column=0)

# global my_label 
# my_label= Label (my_w, text="")
# my_label.grid(row=5, column=0)

l1.bind("<<ListboxSelect>>", my_upd)
e1_str.trace("w", get_data)

my_w.mainloop()



# # from tkinter import *

# # root= Tk()
# # root.geometry("500x300")

# # def update(data):
# #     my_list.delete(0, END)

# #     for item in data:
# #         my_list.insert(END, item)

# # def fillout(e):
# #     my_entry.delete(0, END)
# #     my_entry.insert(0, my_list.get(ACTIVE))

# # def check(e):
# #     typed= my_entry.get()

# #     if typed=="":
# #         data= result
# #     else:
# #         data=[]
# #         for item in result:
# #             if typed in item():
# #                 data.append(item)

# #     update(data)


# # my_label= Label(root, text="Pasirinkite produkta: ",
# #     font=("Helvetica", 14), fg="grey")

# # my_label.pack(pady=20)

# # my_entry= Entry(root, font=("Helvetica", 20))
# # my_entry.pack()

# # my_list= Listbox(root, width=50)
# # my_list.pack(pady=40)



# # update(result)

# # my_list.bind("<<ListboxSelect>>", fillout)
# # my_entry.bind("<KeyRelease>", check)

# # root.mainloop()