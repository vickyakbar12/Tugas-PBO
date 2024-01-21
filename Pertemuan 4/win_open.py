import tkinter as tk
from tkinter import Entry,Button,END, filedialog, Text,LEFT,RIGHT, X

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:\Users\asus\OneDrive\Documents\PUNYA VICKY\Tugas PBO\Pertemuan 4",
        title="Open Text file",
        filetypes=((Text Files, "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf) # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
    
ws = tk.Tk()
ws.title("PythonGuides")
ws.geometry("400x450")
ws["bg"]='#fb0'
txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws,
    text="Open File",
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

ws.mainloop()
    