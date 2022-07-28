import tkinter as tk
import sqlite3

root = tk.Tk()
tk.Label(root, text="Įveskite norimą produktą").grid(row=0)

e1 = tk.Entry(root)
e1.grid(row=0, column=1)

clicked= tk.StringVar()
clicked.set("Pirmadienis")

drop= tk.OptionMenu(root, clicked, "Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis", "Šeštadienis", "Sekmadienis")
drop.grid(row=1, column=1)

# def query():

#     conn= sqlite3.connect("data.db")

#     c= conn.cursor()

#     c.execute("SELECT *, oid FROM produktai")
#     records= c.fetchall()
#     print(records)

#     conn.commit()

#     conn.close()









root.mainloop()