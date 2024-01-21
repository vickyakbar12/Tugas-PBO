import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, W, StringVar, messagebox
from perawat import Perawat

class FormPerawat:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='NIP:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtNIP = Entry(mainFrame) 
        self.txtNIP.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIP.bind("<Return>", self.onCari)  # menambahkan event Enter key

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Jenis Kelamin:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki', value='L', variable=self.txtJK)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.L.select()  # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='Perempuan', value='P', variable=self.txtJK)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idperawat', 'nip', 'nama', 'jk')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idperawat', text='ID')
        self.tree.column('idperawat', width="30")
        self.tree.heading('nip', text='NIP')
        self.tree.column('nip', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIP.delete(0, END)
        self.txtNIP.insert(END, "")
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")       
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data perawat
        perawat = Perawat()
        result = perawat.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        perawats = []
        for row_data in result:
            perawats.append(row_data)

        for perawat_data in perawats:
            self.tree.insert('', END, values=perawat_data)
    
    def onCari(self, event=None):
        nip = self.txtNIP.get()
        perawat = Perawat()
        res = perawat.getBynip(nip)
        rec = perawat.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        nip = self.txtNIP.get()
        perawat = Perawat()
        res = perawat.getBynip(nip)
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, perawat.nama)
        jk = perawat.jk
        if jk == "P":
            self.P.select()
        else:
            self.L.select()
                 
    def onSimpan(self, event=None):
        nip = self.txtNIP.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()
        
        perawat = Perawat()
        perawat.nip = nip
        perawat.nama = nama
        perawat.jk = jk
        if self.ditemukan == True:
            res = perawat.updateBynip(nip)
            ket = 'Diperbarui'
        else:
            res = perawat.simpan()
            ket = 'Disimpan'
            
        rec = perawat.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
            self.onReload()  # Refresh the Treeview
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nip=self.txtNIP.get()
        perawat=Perawat()
        perawat.nip=nip
        if(self.ditemukan==True):
            res=perawat.deleteBynip(nip)
            rec=perawat.affected
        else:
            messagebox.showinfo("showinfo", "Pilih data yang akan dihapus.")

        if(rec>0):
            messagebox.showinfo("showinfo","data berhasil dihapus")

        self.onClear()

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPerawat(root, "Aplikasi Data Perawat")
    root.mainloop()
