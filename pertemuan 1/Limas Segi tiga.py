print("Menghitung luas permukaan dan volume limas segitiga")

#variabel 
alas = 10
tinggi_limas = 12
tinggi_segitiga = 8

#Rumus
luas_permukaan = (alas * tinggi_limas) / 2 + 3 * (0.5 * alas * tinggi_segitiga)
volume = (alas ** 2 * tinggi_segitiga) / 6

#Output
print("Luas Permukaan Limas Segitiga: ", luas_permukaan)
print("Volume Limas Segitiga: ", volume)
