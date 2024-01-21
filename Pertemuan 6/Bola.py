from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class Bola :
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
        Label(mainFrame, text='Jari-jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Bola:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtjari_jari = Entry(mainFrame) 
        self.txtjari_jari.grid(row=0, column=1, padx=5, pady=5)  
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        jari_jari = int(self.txtjari_jari.get())
        luas = round ( 4 * 3.14 * jari_jari ** 2)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = Bola(root, "Program Luas Bola")
    root.mainloop() 