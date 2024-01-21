from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class Balok :
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Lebar:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Panjang:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Balok:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtlebar = Entry(mainFrame) 
        self.txtlebar.grid(row=0, column=1, padx=5, pady=5)  
        self.txttinggi = Entry(mainFrame) 
        self.txttinggi.grid(row=1, column=1, padx=5, pady=5) 
        self.txtpanjang = Entry(mainFrame) 
        self.txtpanjang.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        lebar = int(self.txtlebar.get())
        tinggi = int(self.txttinggi.get())
        panjang = int(self.txtpanjang.get())
        luas = round (2 * (panjang * lebar + panjang * tinggi + lebar * tinggi))
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = Balok(root, "Program Luas Balok")
    root.mainloop() 