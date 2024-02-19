import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Mahasiswa import Mahasiswa
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
class FormMahasiswa:   
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
        
        
         # varchar 
        Label(mainFrame, text='NIM:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NIM
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='NAMA:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA
        self.txtNAMA = Entry(mainFrame) 
        self.txtNAMA.grid(row=1, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='PRODI:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox PRODI
        self.txtPRODI = Entry(mainFrame) 
        self.txtPRODI.grid(row=2, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='KELAS:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox KELAS
        self.txtKELAS = Entry(mainFrame) 
        self.txtKELAS.grid(row=3, column=1, padx=5, pady=5) 
        self.txtKELAS.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # date 
        Label(mainFrame, text='TANGGAL_LAHIR:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL_LAHIR
        self.txtTANGGAL_LAHIR = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL_LAHIR.grid(row=4, column=1, padx=5, pady=5)
                    
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','Nim','nama','prodi','Kelas','Tanggal_Lahir')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('Nim', text='Nim')
        self.tree.column('Nim', width="100")
        self.tree.heading('nama', text='nama')
        self.tree.column('nama', width="100")
        self.tree.heading('prodi', text='prodi')
        self.tree.column('prodi', width="100")
        self.tree.heading('Kelas', text='Kelas')
        self.tree.column('Kelas', width="30")
        self.tree.heading('Tanggal_Lahir', text='Tanggal_Lahir')
        self.tree.column('Tanggal_Lahir', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
                                
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,"")
                                
        self.txtPRODI.delete(0,END)
        self.txtPRODI.insert(END,"")
                                
        self.txtKELAS.delete(0,END)
        self.txtKELAS.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        obj = Mahasiswa()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        Kelas = self.txtKELAS.get()
        obj = Mahasiswa()
        res = obj.getByKELAS(Kelas)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        Kelas = self.txtKELAS.get()
        obj = Mahasiswa()
        res = obj.getByKELAS(Kelas)
            
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,obj.Nim)
                                
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,obj.nama)
                                
        self.txtPRODI.delete(0,END)
        self.txtPRODI.insert(END,obj.prodi)
                                
        self.txtTANGGAL_LAHIR.delete(0,END)
        self.txtTANGGAL_LAHIR.insert(END,obj.Tanggal_Lahir)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        Nim = self.txtNIM.get()
        nama = self.txtNAMA.get()
        prodi = self.txtPRODI.get()
        Kelas = self.txtKELAS.get()
        Tanggal_Lahir = self.txtTANGGAL_LAHIR.get()       
        obj = Mahasiswa()
        obj.Nim = Nim
        obj.nama = nama
        obj.prodi = prodi
        obj.Kelas = Kelas
        obj.Tanggal_Lahir = Tanggal_Lahir
        if(self.ditemukan==True):
            res = obj.updateByKELAS(Kelas)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        Kelas = self.txtKELAS.get()
        obj = Mahasiswa()
        obj.Kelas = Kelas
        if(self.ditemukan==True):
            res = obj.deleteByKELAS(Kelas)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMahasiswa(root, "Aplikasi Data Mahasiswa")
    root.mainloop() 