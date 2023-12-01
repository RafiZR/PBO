import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Video Player")
        
        # Inisialisasi variabel
        self.video_path = None
        self.cap = None

        # Buat widget
        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        self.btn_open = tk.Button(root, text="Open Video",width =15,bg="black",fg="white", command=self.open_video)
        self.btn_open.pack(side=tk.LEFT, padx=5)

        self.btn_play = tk.Button(root, text="Play",width =15,bg="black",fg="white", command=self.play_video)
        self.btn_play.pack(side=tk.LEFT, padx=5)

        self.btn_pause = tk.Button(root, text="Pause",width =15,bg="black",fg="white", command=self.pause_video)
        self.btn_pause.pack(side=tk.LEFT, padx=5)

        self.btn_stop = tk.Button(root, text="Stop",width =15,bg="black",fg="white", command=self.stop_video)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        # Atur status pemutaran video
        self.playing = False

    def open_video(self):
        file_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("MP4 files", "*.mp4")])
        if file_path:
            self.video_path = file_path
            self.cap = cv2.VideoCapture(file_path)
            self.play_video()  # Putar video setelah memilih file

    def play_video(self):
        if self.cap and not self.playing:
            self.playing = True
            self.update_video()

    def pause_video(self):
        self.playing = False

    def stop_video(self):
        if self.cap:
            self.playing = False
            self.cap.release()
            self.canvas.delete("all")

    def update_video(self):
        if self.playing:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(frame)
                self.canvas.config(width=photo.width(), height=photo.height())
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                self.canvas.photo = photo
                self.root.after(30, self.update_video)
            else:
                self.stop_video()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
