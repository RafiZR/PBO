import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    sa = float(txtsisi_alas.get())
    tl = float(txttinggi_limas.get())
    ts = float(txttinggi_segitiga.get())

    L = round((sa ** 2) + 2 * sa * (tl + ts))

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    sa = float(txtsisi_alas.get())
    tl = float(txttinggi_limas.get())
    ts = float(txttinggi_segitiga.get())

    v = round((sa ** 2 * tl) / 3)

    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

#create thinter object
app = tk.Tk()

#Tambahkan Judul
app.title("Kalkulator Luas dan volume Limas segi Empat")

#Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

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
txtsisi_alas = Entry(frame)
txtsisi_alas.grid(row=1, column=1)

#textbox tinggi limas
txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=3, column=1)

#textbox tinggi segitiga
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=2, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung, bg="yellow")
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label (frame, text="Luas: ")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output label volume
volume = Label (frame, text="volume: ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry (frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtvolume = Entry(frame)
txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
