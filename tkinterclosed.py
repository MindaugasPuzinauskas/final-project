# # import tkinter as tk
# # from tkinter import messagebox

# # root = tk.Tk()

# # def on_closing():
# #     if messagebox.askokcancel("Quit", "Do you want to quit?"):
# #         root.destroy()

# # root.protocol("WM_DELETE_WINDOW", on_closing)
# # root.mainloop()

# from tkinter import *
# from tkinter import messagebox

# def callback():
#     if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
#         root.destroy()

# root = Tk()
# root.protocol("WM_DELETE_WINDOW", callback)

# root.mainloop()

# print("labas")





from tkinter import Button


class usr:
    def __str__(self):
        
        self.usiris()
        return self.user
    
    def usiris(self):
        self.user="ona"
        

a=usr()
print(a)


