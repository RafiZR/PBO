print("Menghitung luas permukaan dan volume kerucut")

#variabel 
jari_jari = 8
tinggi = 10
garis_pelukis = 15

# Mengimport nilai pi
from math import pi

#Rumus
luas_permukaan = pi * jari_jari * (jari_jari + garis_pelukis)
volume = (1/3) * pi * (jari_jari ** 2) * tinggi

#Output
print("Luas Permukaan Kerucut: ", luas_permukaan)
print("Volume Kerucut: ", volume)