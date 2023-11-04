import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    a = float(txtalas_segitiga.get())
    ts = float(txttinggi_segitiga.get())
    tp = float(txttinggi_prisma.get())

    L = round(2 * (0.5 * a * ts + a * tp + 0.5 * a * ts))

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    a = float(txtalas_segitiga.get())
    ts = float(txttinggi_segitiga.get())
    tp = float(txttinggi_prisma.get())

    v = round((1/3) * 0.5 * a * ts * tp)

    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

#create thinter object
app = tk.Tk()

#Tambahkan Judul
app.title("Kalkulator Luas dan volume Prisma Segi Tiga")

#Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

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
txtalas_segitiga = Entry(frame)
txtalas_segitiga.grid(row=1, column=1)

#textbox selimut
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=3, column=1)

#textbox tinggi
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=2, column=1)

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
