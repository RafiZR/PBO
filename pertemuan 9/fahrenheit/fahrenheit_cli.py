print("konversi suhu")

#entry
suhu = input("masukan suhu dalam fagrenheit:")

#Rumus
K = (5/9*float(suhu)-32)+273   
R = (4/9*float(suhu)-32)
C = (5/9*float(suhu)-32)

#output
print(suhu + "Kelvin sama dengan")     
print(str(K)+"Kelvin")
print(str(R)+"Reamur")
print(str(C)+"Celcius")