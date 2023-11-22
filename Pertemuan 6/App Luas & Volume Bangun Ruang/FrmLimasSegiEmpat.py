import tkinter as tk
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmLimassegiempat:  
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

        #laber sisi alas
        sisi_alas= Label(frame, text="sisi alas")
        sisi_alas.grid(row=1, column=0, sticky=W , padx=5, pady=5)

        #label tinggi limas
        tinggi_limas= Label(frame, text="tinggi limas")
        tinggi_limas.grid(row=3, column=0, sticky=W , padx=5, pady=5)

        #label tinggi segitiga
        tinggi_segitiga= Label(frame, text="tinggi segitiga")
        tinggi_segitiga.grid(row=2, column=0, sticky=W , padx=5, pady=5)

        #textbox sisi alas
        self.txtsisi_alas = Entry(frame)
        self.txtsisi_alas.grid(row=1, column=1)

        #textbox tinggi limas
        self.txttinggi_limas = Entry(frame)
        self.txttinggi_limas.grid(row=3, column=1)

        #textbox tinggi segitiga
        self.txttinggi_segitiga = Entry(frame)
        self.txttinggi_segitiga.grid(row=2, column=1)

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
        sa = float(self.txtsisi_alas.get())
        tl = float(self.txttinggi_limas.get())
        ts = float(self.txttinggi_segitiga.get())

        L = round((sa ** 2) + 2 * sa * (tl + ts))

        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,L)

    def hitung_volume(self, event=None):
        sa = float(self.txtsisi_alas.get())
        tl = float(self.txttinggi_limas.get())
        ts = float(self.txttinggi_segitiga.get())

        v = round((sa ** 2 * tl) / 3)

        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,v)

    def hitung(self, event=None):
        self.hitung_luas()
        self.hitung_volume()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimassegiempat(root, "Program Luas Volume Segi Empat")
    root.mainloop() 





