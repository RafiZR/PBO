print("konversi suhu")
def get_fahrenheit(suhu):
    F = (9/5*float(suhu))+32
    return F

def get_reamur(suhu):
    R = (4/5*float(suhu))
    return R

def get_kelvin(suhu):
    K = (9/5*float(suhu))+273
    return K

suhu = input("masukan suhu dalam celcius:")

#Rumus
F=get_fahrenheit(suhu)
R=get_reamur(suhu)
K=get_kelvin(suhu)

#output
print(suhu + "celcius sama dengan")
print(str(F)+"Fahrenheit")
print(str(R)+"Reamur")
print(str(K)+"Kelvin")



