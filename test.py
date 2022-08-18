from ctypes import alignment
import tkinter as tk
import sqlite3
from tkinter import *
import re
from turtle import dot, left


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

calories1=0
calories2=0
calories3=0
calories4=0
calories5=0
calories6=0
calories7=0
protein1=0
protein2=0
protein3=0
protein4=0
protein5=0
protein6=0
protein7=0
carbs1=0
carbs2=0
carbs3=0
carbs4=0
carbs5=0
carbs6=0
carbs7=0
fat1=0
fat2=0
fat3=0
fat4=0
fat5=0
fat6=0
fat7=0
sugars1=0
sugars2=0
sugars3=0
sugars4=0
sugars5=0
sugars6=0
sugars7=0

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
    global list_data, calories1, calories2, calories3, calories4, calories5, calories6, calories7
    global protein1, protein2, protein3, protein4, protein5, protein6, protein7
    global carbs1, carbs2, carbs3, carbs4, carbs5, carbs6, carbs7
    global fat1, fat2, fat3, fat4, fat5, fat6, fat7
    global sugars1, sugars2, sugars3, sugars4, sugars5, sugars6, sugars7
    global monday_results, tuesday_results, wednesday_results, thursday_results, friday_results, saturday_results, sunday_results

    # protein3=0
    # protein4=0
    # protein5=0
    # protein6=0
    # protein7=0
    # carbs1=0
    # carbs2=0
    # carbs3=0
    # carbs4=0
    # carbs5=0
    # carbs6=0
    # carbs7=0
    # fat1=0
    # fat2=0
    # fat3=0
    # fat4=0
    # fat5=0
    # fat6=0
    # fat7=0
    # sugars1=0
    # sugars2=0
    # sugars3=0
    # sugars4=0
    # sugars5=0
    # sugars6=0
    # sugars7=0
    con_clk = sqlite3.connect('data.db')
    cur_clk = con_clk.cursor()
    cur_clk.execute("SELECT * FROM produktai WHERE produktas==:product", {"product":content.get()})
    # con.commit()
    sqlresult=cur_clk.fetchone()

    if clk.get()=="Pirmadienis":
        listbox1.insert(tk.END, clk2.get().upper() + ": "+content.get()+ ", * "+str(content1.get()) + "g")
        
        calories1+=((content1.get()/100)*sqlresult[2])
        protein1+=((content1.get()/100)*sqlresult[3])
        carbs1+=((content1.get()/100)*sqlresult[4])
        fat1+=((content1.get()/100)*sqlresult[5])
        sugars1+=((content1.get()/100)*sqlresult[6])
        # monday_results="Viso kalorijų: " + str(round(calories1,1)) + " kcal \nbaltymų: " + str(round(protein1,1)) +  " g\nriebalų: " + str(round(fat1,1)) + " g\nangliavandenių: " + str(round(carbs1,1)) + " g\niš kurių cukrų: " + str(round(sugars1,1)) + " g"
        monday_results="Viso kalorijų:  " + str(round(calories1,1)) + " kcal \nbaltymų:        " + str(round(protein1,1)) +  " g\nriebalų:        " + str(round(fat1,1)) + " g\nangliavandenių: " + str(round(carbs1,1)) + " g\niš kurių cukrų: " + str(round(sugars1,1)) + " g"
    
    elif clk.get()=="Antradienis":
        listbox2.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
        
        calories2+=((content1.get()/100)*sqlresult[2])
        protein2+=((content1.get()/100)*sqlresult[3])
        carbs2+=((content1.get()/100)*sqlresult[4])
        fat2+=((content1.get()/100)*sqlresult[5])
        sugars2+=((content1.get()/100)*sqlresult[6])
        # monday_results="Viso kalorijų: " + str(round(calories1,1)) + " kcal \nbaltymų: " + str(round(protein1,1)) +  " g\nriebalų: " + str(round(fat1,1)) + " g\nangliavandenių: " + str(round(carbs1,1)) + " g\niš kurių cukrų: " + str(round(sugars1,1)) + " g"
        tuesday_results="Viso kalorijų:  " + str(round(calories2,1)) + " kcal \nbaltymų:        " + str(round(protein2,1)) +  " g\nriebalų:        " + str(round(fat2,1)) + " g\nangliavandenių: " + str(round(carbs2,1)) + " g\niš kurių cukrų: " + str(round(sugars2,1)) + " g"
        
    elif clk.get()=="Trečiadienis":
        listbox3.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")
        
        calories3+=((content1.get()/100)*sqlresult[2])
        protein3+=((content1.get()/100)*sqlresult[3])
        carbs3+=((content1.get()/100)*sqlresult[4])
        fat3+=((content1.get()/100)*sqlresult[5])
        sugars3+=((content1.get()/100)*sqlresult[6])
        # monday_results="Viso kalorijų: " + str(round(calories1,1)) + " kcal \nbaltymų: " + str(round(protein1,1)) +  " g\nriebalų: " + str(round(fat1,1)) + " g\nangliavandenių: " + str(round(carbs1,1)) + " g\niš kurių cukrų: " + str(round(sugars1,1)) + " g"
        wednesday_results="Viso kalorijų:  " + str(round(calories3,1)) + " kcal \nbaltymų:        " + str(round(protein3,1)) +  " g\nriebalų:        " + str(round(fat3,1)) + " g\nangliavandenių: " + str(round(carbs3,1)) + " g\niš kurių cukrų: " + str(round(sugars3,1)) + " g"
        
    elif clk.get()=="Ketvirtadienis":
        listbox4.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")


        calories4+=((content1.get()/100)*sqlresult[2])
        protein4+=((content1.get()/100)*sqlresult[3])
        carbs4+=((content1.get()/100)*sqlresult[4])
        fat4+=((content1.get()/100)*sqlresult[5])
        sugars4+=((content1.get()/100)*sqlresult[6])
        # monday_results="Viso kalorijų: " + str(round(calories1,1)) + " kcal \nbaltymų: " + str(round(protein1,1)) +  " g\nriebalų: " + str(round(fat1,1)) + " g\nangliavandenių: " + str(round(carbs1,1)) + " g\niš kurių cukrų: " + str(round(sugars1,1)) + " g"
        thursday_results="Viso kalorijų:  " + str(round(calories4,1)) + " kcal \nbaltymų:        " + str(round(protein4,1)) +  " g\nriebalų:        " + str(round(fat4,1)) + " g\nangliavandenių: " + str(round(carbs4,1)) + " g\niš kurių cukrų: " + str(round(sugars4,1)) + " g"


    elif clk.get()=="Penktadienis":
        listbox5.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")

        calories5+=((content1.get()/100)*sqlresult[2])
        protein5+=((content1.get()/100)*sqlresult[3])
        carbs5+=((content1.get()/100)*sqlresult[4])
        fat5+=((content1.get()/100)*sqlresult[5])
        sugars5+=((content1.get()/100)*sqlresult[6])
        # monday_results="Viso kalorijų: " + str(round(calories1,1)) + " kcal \nbaltymų: " + str(round(protein1,1)) +  " g\nriebalų: " + str(round(fat1,1)) + " g\nangliavandenių: " + str(round(carbs1,1)) + " g\niš kurių cukrų: " + str(round(sugars1,1)) + " g"
        friday_results="Viso kalorijų:  " + str(round(calories5,1)) + " kcal \nbaltymų:        " + str(round(protein5,1)) +  " g\nriebalų:        " + str(round(fat5,1)) + " g\nangliavandenių: " + str(round(carbs5,1)) + " g\niš kurių cukrų: " + str(round(sugars5,1)) + " g"

    elif clk.get()=="Šeštadienis":
        listbox6.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")

        calories6+=((content1.get()/100)*sqlresult[2])
        protein6+=((content1.get()/100)*sqlresult[3])
        carbs6+=((content1.get()/100)*sqlresult[4])
        fat6+=((content1.get()/100)*sqlresult[5])
        sugars6+=((content1.get()/100)*sqlresult[6])
        # monday_results="Viso kalorijų: " + str(round(calories1,1)) + " kcal \nbaltymų: " + str(round(protein1,1)) +  " g\nriebalų: " + str(round(fat1,1)) + " g\nangliavandenių: " + str(round(carbs1,1)) + " g\niš kurių cukrų: " + str(round(sugars1,1)) + " g"
        saturday_results="Viso kalorijų:  " + str(round(calories6,1)) + " kcal \nbaltymų:        " + str(round(protein6,1)) +  " g\nriebalų:        " + str(round(fat6,1)) + " g\nangliavandenių: " + str(round(carbs6,1)) + " g\niš kurių cukrų: " + str(round(sugars6,1)) + " g"
    
    elif clk.get()=="Sekmadienis":
        listbox7.insert(tk.END, clk2.get().upper() + ":  "+content.get()+ ", "+str(content1.get()) + "g")

        calories7+=((content1.get()/100)*sqlresult[2])
        protein7+=((content1.get()/100)*sqlresult[3])
        carbs7+=((content1.get()/100)*sqlresult[4])
        fat7+=((content1.get()/100)*sqlresult[5])
        sugars7+=((content1.get()/100)*sqlresult[6])
        # monday_results="Viso kalorijų: " + str(round(calories1,1)) + " kcal \nbaltymų: " + str(round(protein1,1)) +  " g\nriebalų: " + str(round(fat1,1)) + " g\nangliavandenių: " + str(round(carbs1,1)) + " g\niš kurių cukrų: " + str(round(sugars1,1)) + " g"
        sunday_results="Viso kalorijų:  " + str(round(calories7,1)) + " kcal \nbaltymų:        " + str(round(protein7,1)) +  " g\nriebalų:        " + str(round(fat7,1)) + " g\nangliavandenių: " + str(round(carbs7,1)) + " g\niš kurių cukrų: " + str(round(sugars7,1)) + " g"
    
    list_data.append(content.get())
    results1.set(monday_results)
    results2.set(tuesday_results)
    results3.set(wednesday_results)
    results4.set(thursday_results)
    results5.set(friday_results)
    results6.set(saturday_results)
    results7.set(sunday_results)

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
        m=re.search(': (.*), *', selected1)
        if m:
            product_name = m.group(1)
        n=re.search(',* (\d*)g', selected1)
        if n:
            svoris = n.group(1)

        # start=selected1.find(": ") + len(": ")
        # end= selected1.find(", *")
        # substring=selected1[start:end]
        # print(found)
        con5= sqlite3.connect("data.db")
        cur5= con5.cursor()
        cur5.execute("SELECT * FROM produktai WHERE produktas==:prd", {"prd":product_name})
        result5=(cur5.fetchall())
        # print(result5)
        print(svoris)

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




# -------- LISTBOXES ---------

monday_label=Label(text="PIRMADIENIS")
monday_label.grid(column=1, row=1, padx=5)
listbox1 = tk.Listbox(root, height=10, width=39)
listbox1.grid(column=1, row=2, padx=3)

monday_results=""
results1=StringVar()
results1.set(monday_results)
results1_label=Label(root, textvariable=results1, justify=tk.LEFT)
results1_label.grid(column=1, row=4, rowspan=5, sticky="w")

tuesday_label=Label(text="ANTRADIENIS")
tuesday_label.grid(column=2, row=1)
listbox2 = tk.Listbox(root, width=39)
listbox2.grid(column=2, row=2, padx=3)

tuesday_results=""
results2=StringVar()
results2.set(tuesday_results)
results2_label=Label(root, textvariable=results2, justify=tk.LEFT)
results2_label.grid(column=2, row=4, rowspan=5, sticky="w")

wednesday_label=Label(text="TREČIADIENIS")
wednesday_label.grid(column=3, row=1)
listbox3 = tk.Listbox(root, width=39)
listbox3.grid(column=3, row=2, padx=3)

wednesday_results=""
results3=StringVar()
results3.set(wednesday_results)
results3_label=Label(root, textvariable=results3, justify=tk.LEFT)
results3_label.grid(column=3, row=4, rowspan=5, sticky="w")

thursday_label=Label(text="KETVIRTADIENIS")
thursday_label.grid(column=0, row=9)
listbox4 = tk.Listbox(root, width=39)
listbox4.grid(column=0, row=10, padx=3)

thursday_results=""
results4=StringVar()
results4.set(thursday_results)
results4_label=Label(root, textvariable=results4, justify=tk.LEFT)
results4_label.grid(column=0, row=12, rowspan=5, sticky="w")

friday_label=Label(text="PENKTADIENIS")
friday_label.grid(column=1, row=9)
listbox5 = tk.Listbox(root, width=39)
listbox5.grid(column=1, row=10, padx=3)

friday_results=""
results5=StringVar()
results5.set(friday_results)
results5_label=Label(root, textvariable=results5, justify=tk.LEFT)
results5_label.grid(column=1, row=12, rowspan=5, sticky="w")

saturday_label=Label(text="ŠEŠTADIENIS")
saturday_label.grid(column=2, row=9)
listbox6 = tk.Listbox(root, width=39)
listbox6.grid(column=2, row=10, padx=3)

saturday_results=""
results6=StringVar()
results6.set(saturday_results)
results6_label=Label(root, textvariable=results6, justify=tk.LEFT)
results6_label.grid(column=2, row=12, rowspan=5, sticky="w")

sunday_label=Label(text="SEKMADIENIS")
sunday_label.grid(column=3, row=9)
listbox7 = tk.Listbox(root, width=39)
listbox7.grid(column=3, row=10, padx=3)

sunday_results=""
results7=StringVar()
results7.set(sunday_results)
results7_label=Label(root, textvariable=results7, justify=tk.LEFT)
results7_label.grid(column=3, row=12, rowspan=5, sticky="w")
#BUTTONS 
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
button_delete_selected4.grid(column=0, row=11, sticky="w")

button_delete_selected5 = tk.Button(text="Delete Selected", command=delete_selected5)
button_delete_selected5.grid(column=1, row=11, sticky="w")

button_delete_selected6 = tk.Button(text="Delete Selected", command=delete_selected6)
button_delete_selected6.grid(column=2, row=11, sticky="w")

button_delete_selected7 = tk.Button(text="Delete Selected", command=delete_selected7)
button_delete_selected7.grid(column=3, row=11, sticky="w")

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

l1= tk.Listbox(root, height=10, width=39, relief="flat",
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

root.mainloop()

