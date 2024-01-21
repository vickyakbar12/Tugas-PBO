import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W
from math import pi

def hitung_luas():
    jari_jari = float(txtjari_jari.get())
    tinggi = float(txttinggi.get())
    
    L = 2 * pi * jari_jari * (jari_jari + tinggi)
    
    txtluas.delete(0,END)
    txtluas.insert(END,L)
    
def hitung_Volume():
    jari_jari = float(txtjari_jari.get())
    tinggi = float(txttinggi.get())
    
    V = pi * (jari_jari ** 2) * tinggi
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,V)
    
def hitung():
    hitung_luas()
    hitung_Volume()
    
# Creat tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulaor Luas dan Volume Tabung")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label jari_jari
jari_jari = Label(frame, text="jari jari:")
jari_jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label tinggi
tinggi = Label(frame, text="tinggi:")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox jari_jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1)

# Textbox tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas:")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
Volume = Label(frame, text="Volume:")
Volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas 
txtluas = Entry(frame)
txtluas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
