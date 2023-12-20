print("konversi suhu")

#entry
suhu = input("masukan suhu dalam kelvin:")

#Rumus
R = (4/5*float(suhu)-273)   
F = (9/5*float(suhu)-273)+32
C = (float(suhu))-273

#output
print(suhu + "Kelvin sama dengan")     
print(str(F)+"Fahrenheit")
print(str(R)+"Reamur")
print(str(C)+"Celcius")