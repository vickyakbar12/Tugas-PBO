import tkinter as tk
from tkinter import Entry,Button,END, filedialog, Text, LEFT, RIGHT, X

def openfile():
    tf=filedialog.askopenfilename(
        initialdir="C:/Users/Lenovo/Documents/KULIAH SEMESTER 3/PBO/Pertemuan 4", 
        title="Open Text file",
        filetypes=(("Text File", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf=open(tf) #or tf=open(tf, 'r')
    data=tf.read()
    txtarea.insert(END, data)
    tf.close()
    
def savefile():
    teks=pathh.get()
    with open(pathh.get(),"w") as file1:
        file1.write(txtarea.get(1.0, "end-1c"))
        
        txtarea.delete(1.0, "end-1c")
        file1.close()
       
ws=tk.Tk()
ws.title("PythonGuides")
ws.geometry("400x450")
ws['bg']='#fb0'
txtarea=Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh= Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws,
    text="Open File",
    command=openfile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

Button(
    ws,
    text="Save File",
    command=savefile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

ws.mainloop()