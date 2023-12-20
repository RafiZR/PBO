print("konversi suhu")
def get_fahrenheit(suhu):
    F = (9/5*float(suhu)-273)+32
    return F

def get_celcius(suhu):
    C = (float(suhu))-273
    return C

def get_reamur(suhu):
    R = (4/5*float(suhu)-273)
    return R

#entry
suhu = input("masukan suhu dalam kelvin:")

#Rumus
F=get_fahrenheit(suhu)
C=get_celcius(suhu)
R=get_reamur(suhu)

#output
print(suhu + "Kelvin sama dengan")
print(str(F)+"Fahrenheit")
print(str(C)+"Celcius")
print(str(R)+"Reamur")



