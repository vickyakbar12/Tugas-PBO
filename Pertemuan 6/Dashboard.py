import tkinter as tk
from tkinter import Menu

from Balok import *
from Bola import *
from Kubus import *
from Kerucut import *
from Limas_Segiempat import *
from Limas_Segitiga import *
from Prisma_Segitiga import *
from Tabung import *

# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
#data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Balok', command= lambda: new_window("Luas Balok", Balok)
)
app_menu.add_command(
    label='App Bola', command= lambda: new_window("Luas Bola", Bola)
)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Luas Kerucut", Kerucut)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Luas Kubus", Kubus)
)
app_menu.add_command(
    label='App Limas_Segiempat', command= lambda: new_window("Luas Limas_Segiempat", Limas_Segiempat)
)
app_menu.add_command(
    label='App Limas_Segitiga', command= lambda: new_window("Luas Limas_Segitiga", Limas_Segitiga)
)
app_menu.add_command(
    label='App Prisma_Segitiga', command= lambda: new_window("Luas Prisma_Segitiga", Prisma_Segitiga)
)
app_menu.add_command(
    label='App Tabung', command= lambda: new_window("Luas Tabung", Tabung)
)

def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
    
root.mainloop()