from calendar import FRIDAY
import tkinter as tk
import sqlite3
from tkinter import *
import re
from turtle import dot



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

root = tk.Tk()
root.title("Produktų pasirinkimas")
root.geometry("1600x2560")
list_data = []


#--------------------------------------------------------------------------------------------------------

frame1=Frame(root, width=5)
# def retrievedata():
#  global list_data
#  list_data = []
#  try:
#   with open("save.txt", "r", encoding="utf-8") as file:
#    for f in file:
#     listbox.insert(tk.END, f.strip())
#     list_data.append(f.strip())
#     print(list_data)
#  except:
#   pass

def clicked():
    global list_data
    if clk.get()=="Pirmadienis":
        listbox1.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
    elif clk.get()=="Antradienis":
        listbox2.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
    elif clk.get()=="Trečiadienis":
        listbox3.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
    elif clk.get()=="Ketvirtadienis":
        listbox4.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
    elif clk.get()=="Penktadienis":
        listbox5.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
    elif clk.get()=="Šeštadienis":
        listbox6.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
    elif clk.get()=="Sekmadienis":
        listbox7.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
    list_data.append(content.get())

def delete():
    global list_data
    listbox1.delete(0, tk.END)
    listbox2.delete(0, tk.END)
    listbox3.delete(0, tk.END)
    listbox4.delete(0, tk.END)
    listbox5.delete(0, tk.END)
    listbox6.delete(0, tk.END)
    listbox7.delete(0, tk.END)
    list_data = []

def delete_selected1():
    global list_data

    try:
        selected1= listbox1.get(listbox1.curselection())
        listbox1.delete(tk.ANCHOR)
        list_data.pop(list_data.index(selected1))
    except:
        pass

def delete_selected2():
    global list_data

    try:
        selected2= listbox2.get(listbox2.curselection())
        listbox2.delete(tk.ANCHOR)
        list_data.pop(list_data.index(selected2))
    except:
        pass

def delete_selected3():
    global list_data

    try:
        selected3= listbox3.get(listbox3.curselection())
        listbox3.delete(tk.ANCHOR)
        list_data.pop(list_data.index(selected3))
    except:
        pass

def delete_selected4():
    global list_data

    try:
        selected4= listbox4.get(listbox4.curselection())
        listbox4.delete(tk.ANCHOR)
        list_data.pop(list_data.index(selected4))
    except:
        pass

def delete_selected5():
    global list_data

    try:
        selected5= listbox5.get(listbox5.curselection())
        listbox5.delete(tk.ANCHOR)
        list_data.pop(list_data.index(selected5))
    except:
        pass

def delete_selected6():
    global list_data

    try:
        selected6= listbox6.get(listbox6.curselection())
        listbox6.delete(tk.ANCHOR)
        list_data.pop(list_data.index(selected6))
    except:
        pass

def delete_selected7():
    global list_data

    try:
        selected7= listbox7.get(listbox7.curselection())
        listbox7.delete(tk.ANCHOR)
        list_data.pop(list_data.index(selected7))
    except:
        pass

def quit():
    global root
    # con = sqlite3.connect('userdatatest.db')
    # cur = con.cursor()
    # cur.execute()
    with open("save.txt", "w", encoding="utf-8") as file:
        for d in list_data:
            file.write(d + "\n")
    root.destroy()

# LISTBOX

# weekday=Label(root, text= "Pasirinkite savaitės dieną: ", justify=LEFT, anchor="w")
# weekday.grid(sticky=W, column=0, row=0)

clk= StringVar()
clk.set("Pirmadienis")

drop2= OptionMenu(root, clk, "Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis", "Šeštadienis", "Sekmadienis")
drop2.grid(column=0, row=3, sticky="w")
#-------------------
# meal=Label(root, text="Pasirinkite valgymo metą: ", justify=LEFT, anchor="w")
# meal.grid(sticky=W, column=0, row=2)

clk2= StringVar()
clk2.set("Pusryčiai")

drop1= OptionMenu(root, clk2, "Pusryčiai", "Pietūs", "Vakarienė")
drop1.grid(column=0, row=3)

#-------------------
product=Label(root, text="Pasirinkite produktą")
product.grid(column=0, row=0, sticky="w")

content = tk.StringVar()
entry = tk.Entry(root, textvariable=content)
entry.grid(column=0, row=1)

quantity_label=Label(root, text="Įveskite kiekį gramais")
quantity_label.grid(column=0,row=4, sticky="w")

content1 = tk.IntVar()
quantity=tk.Entry(root,textvariable=content1)
quantity.grid(column=0, row=5, sticky="w")


button = tk.Button(root, text="Add Item", command=clicked)
button.grid(column=0, row=6, sticky="w")

button_delete = tk.Button(text="Clear all", command=delete)
button_delete.grid(column=0, row=6)

button_delete_selected1 = tk.Button(text="Delete Selected", command=delete_selected1)
button_delete_selected1.grid(column=1, row=3, sticky="w")

button_delete_selected2 = tk.Button(text="Delete Selected", command=delete_selected2)
button_delete_selected2.grid(column=2, row=3, sticky="w")

button_delete_selected3 = tk.Button(text="Delete Selected", command=delete_selected3)
button_delete_selected3.grid(column=3, row=3, sticky="w")

button_delete_selected4 = tk.Button(text="Delete Selected", command=delete_selected4)
button_delete_selected4.grid(column=0, row=15, sticky="w")

button_delete_selected5 = tk.Button(text="Delete Selected", command=delete_selected5)
button_delete_selected5.grid(column=1, row=15, sticky="w")

button_delete_selected6 = tk.Button(text="Delete Selected", command=delete_selected6)
button_delete_selected6.grid(column=2, row=15, sticky="w")

button_delete_selected7 = tk.Button(text="Delete Selected", command=delete_selected7)
button_delete_selected7.grid(column=3, row=15, sticky="w")

# -------- LISTBOXES ---------

Monday_label=Label(text="PIRMADIENIS")
Monday_label.grid(column=1, row=1, padx=10)
listbox1 = tk.Listbox(root, height=10, width=40)
listbox1.grid(column=1, row=2, padx=5)

Tuesday_label=Label(text="ANTRADIENIS")
Tuesday_label.grid(column=2, row=1)
listbox2 = tk.Listbox(root, width=40)
listbox2.grid(column=2, row=2, padx=5)

Wednesday_label=Label(text="TREČIADIENIS")
Wednesday_label.grid(column=3, row=1)
listbox3 = tk.Listbox(root, width=40)
listbox3.grid(column=3, row=2, padx=5)

Thursday_label=Label(text="KETVIRTADIENIS")
Thursday_label.grid(column=0, row=13)
listbox4 = tk.Listbox(root, width=40)
listbox4.grid(column=0, row=14, padx=5)

Friday_label=Label(text="PENKTADIENIS")
Friday_label.grid(column=1, row=13)
listbox5 = tk.Listbox(root, width=40)
listbox5.grid(column=1, row=14, padx=5)

Saturday_label=Label(text="ŠEŠTADIENIS")
Saturday_label.grid(column=2, row=13)
listbox6 = tk.Listbox(root, width=40)
listbox6.grid(column=2, row=14, padx=5)

Sunday_label=Label(text="SEKMADIENIS")
Sunday_label.grid(column=3, row=13)
listbox7 = tk.Listbox(root, width=40)
listbox7.grid(column=3, row=14, padx=5)

Results1=Label(text="Rezultatai")
Results1.grid(column=0, row=9, sticky="w")

bquit = tk.Button(root, text="Quit and save", command=quit)
bquit.grid(column=0, row=6, sticky="e")





con2= sqlite3.connect("data.db")
cur2= con2.cursor()
statement= "SELECT produktas FROM produktai"
cur2.execute(statement)
result=(cur2.fetchall())

my_list=[r for r, in result]

def my_upd(my_widget):
    my_w= my_widget.widget
    index= int (my_w.curselection()[0])
    value= my_w.get(index)
    content.set(value)
    l1.delete(0, END)

def my_down(my_widget):
    l1.focus()
    l1.selection_set(0)

l1= tk.Listbox(root, height=10, width=40, relief="flat",
    bg="black", highlightcolor= "white")
l1.grid(column=0, row=2)

def get_data(*args):
    search_str=entry.get()
    l1.delete(0, END)
    for element in my_list:
        if(re.match(search_str, element, re.IGNORECASE)):
            l1.insert(tk.END, element)

l1.bind("<<ListboxSelect>>", my_upd)
content.trace("w", get_data)

#retrievedata()
root.mainloop()


# import sqlite3

# def getAllRows():
#     try:
#         connection= sqlite3.connect("data.db")
#         cursor= connection.cursor()
#         print("Connected")

#         sqlite_select_query= ''' SELECT * from produktai'''
#         cursor.execute(sqlite_select_query)
#         records= cursor.fetchall()
#         print("Total rows are: ", len(records))
#         print("Printing each row")
#         for row in records:
#             print("ID: ", row[0])
#             print("Produktas: ", row[1])
#             print("Kalorijos: ", row[2])
#             print("baltymai: ", row[3])
#             print("angliavandeniai: ", row[4])
#             print("riebalai: ", row[5])
#             print("Cukrus: ", row[6])
#             print("\n")

#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to read data from table", error)
#     finally:
#         if connection:
#             connection.close()
#             print("The Sqlite connection is closed")

# getAllRows()
