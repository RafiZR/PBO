import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())

    L = round(pj * lb)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_Keliling():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())

    K = round(2 * (pj + lb))

    txtKeliling.delete(0,END)
    txtKeliling.insert(END,K)

def hitung():
    hitung_luas()
    hitung_Keliling()

#create thinter object
app = tk.Tk()

#Tambahkan Judul
app.title("Kalkulator Luas dan Keliling persegi Panjang")

#Windows
frame = Frame(app)
frame.pack(padx=130, pady=30)

#Label Nama
nama= Label(frame, text="Rafi Zaidan Rabbani (220511074)", bg="yellow", fg="blue")
nama.grid(row=0, column=0, sticky=W , padx=5, pady=5)

#laber panjang
panjang= Label(frame, text="panjang")
panjang.grid(row=1, column=0, sticky=W , padx=5, pady=5)

#label lebar
lebar= Label(frame, text="lebar")
lebar.grid(row=2, column=0, sticky=W , padx=5, pady=5)

#textbox panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=1, column=1)

#textbox lebar
txtlebar = Entry(frame)
txtlebar.grid(row=2, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung, bg="yellow")
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label (frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output label Keliling
keliling = Label (frame, text="Keliling: ")
keliling.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry (frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtKeliling = Entry(frame)
txtKeliling.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
