import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    r = float(txtjari_jari.get())

    from math import pi

    L = round(4*pi*(r*r))

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtjari_jari.get())

    from math import pi
    v = round(4/3*pi*(r*r*r))

    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

#create thinter object
app = tk.Tk()

#Tambahkan Judul
app.title("Kalkulator Luas dan volume Bola")

#Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

#Label Nama
nama= Label(frame, text="Rafi Zaidan Rabbani (220511074)", bg="yellow", fg="blue")
nama.grid(row=0, column=0, sticky=W , padx=5, pady=5)

#laber jari-jari
jari_jari= Label(frame, text="jari-jari")
jari_jari.grid(row=1, column=0, sticky=W , padx=5, pady=5)

#textbox jari-jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung, bg="yellow")
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label (frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label volume
volume = Label (frame, text="volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry (frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtvolume = Entry(frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
