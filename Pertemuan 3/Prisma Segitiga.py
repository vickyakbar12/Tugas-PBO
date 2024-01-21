import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    alas_segitiga = float(txtalas_segitiga.get())
    tinggi_prisma = float(txttinggi_prisma.get())
    tinggi_segitiga = float (txttinggi_segitiga.get())
    
    L = (alas_segitiga * tinggi_prisma) + 2 * (0.5 * alas_segitiga * tinggi_segitiga)
    
    txtluas.delete(0,END)
    txtluas.insert(END,L)
    
def hitung_Volume():
    alas_segitiga = float(txtalas_segitiga.get())
    tinggi_prisma = float(txttinggi_prisma.get())
    tinggi_segitiga = float (txttinggi_segitiga.get())
    
    V = 0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,V)
    
def hitung():
    hitung_luas()
    hitung_Volume()
    
# Creat tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulaor Luas dan Volume Prisma Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label alas_segitiga
alas_segitiga = Label(frame, text="alas segitiga:")
alas_segitiga.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label tinggi limas
tinggi_prisma = Label(frame, text="tinggi limas:")
tinggi_prisma.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label tinggi segitiga
tinggi_segitiga = Label(frame, text="tinggi segitiga:")
tinggi_segitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox alas_segitiga
txtalas_segitiga = Entry(frame)
txtalas_segitiga.grid(row=0, column=1)

# Textbox tinggi limas
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=1, column=1)

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
