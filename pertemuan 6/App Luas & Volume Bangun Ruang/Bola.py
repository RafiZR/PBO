import tkinter as tk
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from math import pi

class FrmBola:  
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
        jari_jari= Label(frame, text="jari-jari")
        jari_jari.grid(row=1, column=0, sticky=W , padx=5, pady=5)

        #textbox jari-jari
        self.txtjari_jari = Entry(frame)
        self.txtjari_jari.grid(row=1, column=1)

        # Button
        hitung_button = Button (frame, text="Hitung", command=self.hitung)
        hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # Output Label Luas
        luas = Label (frame, text="Luas: ")
        luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        # Output label volume
        volume = Label (frame, text="volume: ")
        volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Output Textbox Luas
        self.txtLuas = Entry (frame)
        self.txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # Output Textbox volume
        txtvolume = Entry(frame)
        txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

    def hitung_luas(self, event=None):
        r = float(self.txtjari_jari.get())

        L = round(4*pi*(r*r))

        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,L)

    def hitung_volume(self, event=None):
        r = float(self.txtjari_jari.get())

        v = round(4/3*pi*(r*r*r))

        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,v)

    def hitung(self, event=None):
        self.hitung_luas()
        self.hitung_volume()


if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmBola(root, "Program Luas & Volume Bola")
    root.mainloop() 

