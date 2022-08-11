# import tkinter as tk


# root = tk.Tk()
# root.title("Produktų pasirinkimas")
# root.geometry("400x400")

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

# def clicked():
#     global list_data
#     listbox.insert(tk.END, content.get())
#     list_data.append(content.get())

# def delete():
#     global list_data
#     listbox.delete(0, tk.END)
#     list_data = []

# def delete_selected():
#     global list_data

#     try:
#         selected = listbox.get(listbox.curselection())
#         listbox.delete(tk.ANCHOR)
        
#         list_data.pop(list_data.index(selected))
#     except:
#         pass

# def quit():
#  global root
#  with open("save.txt", "w", encoding="utf-8") as file:
#   for d in list_data:
#    file.write(d + "\n")
#  root.destroy()

# # LISTBOX

# content = tk.StringVar()
# entry = tk.Entry(root, textvariable=content)
# entry.pack()

# button = tk.Button(root, text="Add Item", command=clicked)
# button.pack()

# button_delete = tk.Button(text="Delete", command=delete)
# button_delete.pack()

# button_delete_selected = tk.Button(text="Delete Selected", command=delete_selected)
# button_delete_selected.pack()

# listbox = tk.Listbox(root)
# listbox.pack()

# bquit = tk.Button(root, text="Quit and save", command=quit)
# bquit.pack()

# retrievedata()
# root.mainloop()


import sqlite3

def getAllRows():
    try:
        connection= sqlite3.connect("data.db")
        cursor= connection.cursor()
        print("Connected")

        sqlite_select_query= ''' SELECT * from produktai'''
        cursor.execute(sqlite_select_query)
        records= cursor.fetchall()
        print("Total rows are: ", len(records))
        print("Printing each row")
        for row in records:
            print("ID: ", row[0])
            print("Produktas: ", row[1])
            print("Kalorijos: ", row[2])
            print("baltymai: ", row[3])
            print("angliavandeniai: ", row[4])
            print("riebalai: ", row[5])
            print("Cukrus: ", row[6])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if connection:
            connection.close()
            print("The Sqlite connection is closed")

getAllRows()
