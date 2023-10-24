print("Menghitung luas permukaan dan volume limas segi empat")

#variabel 
sisi_alas = 7
tinggi_limas = 10
tinggi_segitiga = 8

#Rumus
luas_permukaan = (sisi_alas ** 2) + 2 * sisi_alas * (tinggi_limas + tinggi_segitiga)
volume = (sisi_alas ** 2 * tinggi_limas) / 3

#Output
print("Luas Permukaan Limas Segi Empat: ", luas_permukaan)
print("Volume Limas Segi Empat: ", volume)