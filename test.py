import tkinter as tk


root = tk.Tk()
root.title("Produktų pasirinkimas")
root.geometry("400x400")

def retrievedata():
 global list_data
 list_data = []
 try:
  with open("save.txt", "r", encoding="utf-8") as file:
   for f in file:
    listbox.insert(tk.END, f.strip())
    list_data.append(f.strip())
    print(list_data)
 except:
  pass

def clicked():
    global list_data
    listbox.insert(tk.END, content.get())
    list_data.append(content.get())

def delete():
    global list_data
    listbox.delete(0, tk.END)
    list_data = []

def delete_selected():
    global list_data

    try:
        selected = listbox.get(listbox.curselection())
        listbox.delete(tk.ANCHOR)
        
        list_data.pop(list_data.index(selected))
    except:
        pass

def quit():
 global root
 with open("save.txt", "w", encoding="utf-8") as file:
  for d in list_data:
   file.write(d + "\n")
 root.destroy()

# LISTBOX

content = tk.StringVar()
entry = tk.Entry(root, textvariable=content)
entry.pack()

button = tk.Button(root, text="Add Item", command=clicked)
button.pack()

button_delete = tk.Button(text="Delete", command=delete)
button_delete.pack()

button_delete_selected = tk.Button(text="Delete Selected", command=delete_selected)
button_delete_selected.pack()

listbox = tk.Listbox(root)
listbox.pack()

bquit = tk.Button(root, text="Quit and save", command=quit)
bquit.pack()

retrievedata()
root.mainloop()