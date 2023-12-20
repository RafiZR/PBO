print("konversi suhu")

#entry
suhu = input("masukan suhu dalam Reamur:")

#Rumus
C = (5/4*float(suhu))
F = (9/4*float(suhu))+32
K = (5/4*float(suhu))+273

#output
print(suhu + "reamur sama dengan")
print(str(C)+"celcius")
print(str(F)+"fahrenheit")
print(str(K)+"Kelvin")