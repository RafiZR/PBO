import tkinter as tk
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmPrismaSegiTiga:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        frame = Frame(self.parent, bd=10)
        frame.pack(fill=BOTH, expand=YES)

        #Label Nama
        nama= Label(frame, text="Rafi Zaidan Rabbani (220511074)", bg="yellow", fg="blue")
        nama.grid(row=0, column=0, sticky=W , padx=5, pady=5)

        #laber jari-jari
        alas_segitiga= Label(frame, text="alas segitiga")
        alas_segitiga.grid(row=1, column=0, sticky=W , padx=5, pady=5)

        #label selimut
        tinggi_segitiga= Label(frame, text="tinggi segitiga")
        tinggi_segitiga.grid(row=3, column=0, sticky=W , padx=5, pady=5)

        #label tinggi
        tinggi_prisma= Label(frame, text="tinggi prisma")
        tinggi_prisma.grid(row=2, column=0, sticky=W , padx=5, pady=5)

        #textbox jari-jari
        self.txtalas_segitiga = Entry(frame)
        self.txtalas_segitiga.grid(row=1, column=1)

        #textbox selimut
        self.txttinggi_segitiga = Entry(frame)
        self.txttinggi_segitiga.grid(row=3, column=1)

        #textbox tinggi
        self.txttinggi_prisma = Entry(frame)
        self.txttinggi_prisma.grid(row=2, column=1)

        # Button
        hitung_button = Button (frame, text="Hitung", command=self.hitung)
        hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        # Output Label Luas
        luas = Label (frame, text="Luas: ")
        luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        # Output label volume
        volume = Label (frame, text="volume: ")
        volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        # Output Textbox Luas
        self.txtLuas = Entry (frame)
        self.txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

        # Output Textbox volume
        self.txtvolume = Entry(frame)
        self.txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()   
        
    def hitung_luas(self, event=None):
        a = float(self.txtalas_segitiga.get())
        ts = float(self.txttinggi_segitiga.get())
        tp = float(self.txttinggi_prisma.get())

        L = round(2 * (0.5 * a * ts + a * tp + 0.5 * a * ts))

        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,L)

    def hitung_volume(self, event=None):
        a = float(self.txtalas_segitiga.get())
        ts = float(self.txttinggi_segitiga.get())
        tp = float(self.txttinggi_prisma.get())

        v = round((1/3) * 0.5 * a * ts * tp)

        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,v)

    def hitung(self, event=None):
        self.hitung_luas()
        self.hitung_volume()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPrismaSegiTiga(root, "Program Luas & Volume Prisma Segi Tiga")
    root.mainloop() 