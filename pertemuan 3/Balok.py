import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())

    L = round((2*p*t)+(2*p*t)+(2*p*t))

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())

    v = round(p*l*t)  

    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

#create thinter object
app = tk.Tk()

#Tambahkan Judul
app.title("Kalkulator Luas dan volume Balok")

#Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

#Label Nama
nama= Label(frame, text="Rafi Zaidan Rabbani (220511074)", bg="yellow", fg="blue")
nama.grid(row=0, column=0, sticky=W , padx=5, pady=5)

#laber panjang
panjang= Label(frame, text="panjang")
panjang.grid(row=1, column=0, sticky=W , padx=5, pady=5)

#label lebar
lebar= Label(frame, text="lebar")
lebar.grid(row=3, column=0, sticky=W , padx=5, pady=5)

#label tinggi
tinggi= Label(frame, text="tinggi")
tinggi.grid(row=2, column=0, sticky=W , padx=5, pady=5)

#textbox panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=1, column=1)

#textbox lebar
txtlebar = Entry(frame)
txtlebar.grid(row=3, column=1)

#textbox tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

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
