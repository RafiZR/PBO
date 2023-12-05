import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pytesseract import image_to_string, pytesseract
import os

class ImageToTextConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")

        # Tambahkan path menuju Tesseract
        pytesseract.tesseract_cmd = r'C:\Users\M S I\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        browse_button = tk.Button(root, text="Browse", command=self.browse_image)
        browse_button.pack(pady=10)

        convert_button = tk.Button(root, text="Convert", command=self.convert_image)
        convert_button.pack(pady=10)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)

        self.file_path = ""

    def browse_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.file_path:
            self.display_image()

    def display_image(self):
        img = Image.open(self.file_path)
        img.thumbnail((400, 400))
        img = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img)
        self.image_label.image = img

    def convert_image(self):
        if self.file_path:
            img = Image.open(self.file_path)
            text = image_to_string(img)
            self.result_text.delete(1.0, tk.END)  # Clear previous text
            self.result_text.insert(tk.END, text)
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please select an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextConverterApp(root)
    root.mainloop()
