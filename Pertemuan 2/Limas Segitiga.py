import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    alas = float(txtalas.get())
    tinggi_limas = float(txttinggi_limas.get())
    tinggi_segitiga = float (txttinggi_segitiga.get())
    
    L = (alas * tinggi_limas) / 2 + 3 * (0.5 * alas * tinggi_segitiga)
    
    txtluas.delete(0,END)
    txtluas.insert(END,L)
    
def hitung_Volume():
    alas = float(txtalas.get())
    tinggi_limas = float(txttinggi_limas.get())
    tinggi_segitiga = float (txttinggi_segitiga.get())
    
    V = (alas ** 2 * tinggi_segitiga) / 6
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,V)
    
def hitung():
    hitung_luas()
    hitung_Volume()
    
# Creat tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulaor Luas dan Volume Limas Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label alas
alas = Label(frame, text="sisi alas:")
alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label tinggi limas
tinggi_limas = Label(frame, text="tinggi limas:")
tinggi_limas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label tinggi segitiga
tinggi_segitiga = Label(frame, text="tinggi segitiga:")
tinggi_segitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox alas
txtalas = Entry(frame)
txtalas.grid(row=0, column=1)

# Textbox tinggi limas
txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=1, column=1)

# Textbox tinggi segitiga
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
Volume = Label(frame, text="Volume:")
Volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas 
txtluas = Entry(frame)
txtluas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
