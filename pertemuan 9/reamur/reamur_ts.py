print("konversi suhu")
def get_fahrenheit(suhu):
    F = (9/5*float(suhu))+32
    return F

def get_celcius(suhu):
    C = (5/4*float(suhu))
    return C

def get_kelvin(suhu):
    K = (5/4*float(suhu))+273
    return K

#entry
suhu = input("masukan suhu dalam reamur:")

#Rumus
F=get_fahrenheit(suhu)
C=get_celcius(suhu)
K=get_kelvin(suhu)

#output
print(suhu + "Reamur sama dengan")
print(str(F)+"Fahrenheit")
print(str(C)+"Celcius")
print(str(K)+"Kelvin")



