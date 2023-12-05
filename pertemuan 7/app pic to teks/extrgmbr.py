from PIL import Image
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'C:\Users\M S I\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Dapatkan path absolut ke direktori skrip
script_dir = os.path.dirname(os.path.abspath(__file__))

#Define path to image
path_to_image = os.path.join(script_dir, "picture.jpg")

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)