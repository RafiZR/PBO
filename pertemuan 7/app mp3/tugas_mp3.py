import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.master.geometry("360x180")

        self.playlist = []
        self.current_index = 0

        self.setup_ui()

    def setup_ui(self):
        # Button untuk memilih file MP3
        self.add_button = tk.Button(self.master, text="Add Song", width =10,bg="black",fg="yellow", command=self.add_song)
        self.add_button.grid(row=1,column=0,columnspan=1)
        # Button untuk memainkan atau menghentikan lagu
        self.play_button=tk.Button(root,text="Play",width =10,bg="black",fg="yellow", command=self.play_pause)
        self.play_button.grid(row=1,column=1,columnspan=1)
        # Listbox untuk menampilkan daftar playlist
        self.playlist_listbox = tk.Listbox(self.master,width=60, height=10,bg="black",fg="white", selectmode=tk.SINGLE)
        self.playlist_listbox.grid(row=2,column=0,columnspan=4)
        # Button untuk memainkan lagu berikutnya
        self.next_button = tk.Button(self.master, text="Next", width =10,bg="black",fg="yellow", command=self.next_song)
        self.next_button.grid(row=1,column=3,columnspan=1)
        # Button untuk memainkan lagu sebelumnya
        self.prev_button = tk.Button(self.master, text="Previous",bg="black",fg="yellow", width =10, command=self.prev_song)
        self.prev_button.grid(row=1,column=2,columnspan=1)
        

        # Inisialisasi pygame mixer
        pygame.mixer.init()

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if song_path:
            song_name = os.path.basename(song_path)
            self.playlist.append((song_name, song_path))
            self.playlist_listbox.insert(tk.END, song_name)

    def play_pause(self):
        if  pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.play_button.config(text="Play")
        else:
            if not self.playlist:
                return
            song_name, song_path = self.playlist[self.current_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            self.play_button.config(text="Pause")

    def next_song(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_song()

    def prev_song(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_song()

    def play_song(self):
        if not self.playlist:
            return
        song_name, song_path = self.playlist[self.current_index]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        self.play_button.config(text="Pause")

# Membuat instance Tkinter
root = tk.Tk()
app = MP3Player(root)

# Menjalankan loop Tkinter
root.mainloop()
