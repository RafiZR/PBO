print("Menghitung luas permukaan dan volume prisma segitiga")

#variabel 
alas_segitiga = 16
tinggi_segitiga = 14
tinggi_prisma = 18

#Rumus
luas_permukaan = (alas_segitiga * tinggi_prisma) + 2 * (0.5 * alas_segitiga * tinggi_segitiga)
volume = 0.5 * alas_segitiga * tinggi_segitiga * tinggi_prisma

#Output
print("Luas Permukaan Prisma Segitiga: ", luas_permukaan)
print("Volume Prisma Segitiga: ", volume)
