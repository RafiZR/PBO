from gtts import gTTS
import os
import tkinter as tk
from tkinter import scrolledtext

def convert_to_speech():
    # Ambil teks dari input pengguna
    text_to_speak = text_entry.get("1.0",'end-1c')

    # Cek apakah teks kosong

    try:
        # Konversi teks ke suara
        tts = gTTS(text=text_to_speak, lang='ja')  # Ganti 'id' dengan kode bahasa yang diinginkan
        tts.save("output.mp3")

        # Mainkan suara menggunakan perintah sistem
        os.system("start output.mp3")

        result_text.config(text="Suara berhasil diputar!")
    except Exception as e:
        result_text.config(text=f"Terjadi kesalahan: {str(e)}")

# Membuat GUI menggunakan Tkinter
app = tk.Tk()
app.title("Text-to-Speech Converter")

# Label dan Input untuk Teks
text_label = tk.Label(app, text="Masukkan Teks:")
text_label.pack()

text_entry = scrolledtext.ScrolledText(app, width=40, height=10)
text_entry.pack()

# Tombol untuk mengubah teks menjadi suara
convert_button = tk.Button(app, text="Ubah ke Suara", command=convert_to_speech)
convert_button.pack()

# Label untuk hasil
result_text = tk.Label(app, text="")
result_text.pack()

# Menjalankan aplikasi Tkinter
app.mainloop()
