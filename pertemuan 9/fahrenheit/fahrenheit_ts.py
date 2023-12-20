print("konversi suhu")
def get_kelvin(suhu):
    K = (5/9*float(suhu)-32)+273
    return K

def get_celcius(suhu):
    C = (5/9*float(suhu)-32)
    return C

def get_reamur(suhu):
    R = (4/9*float(suhu)-32)
    return R

#entry
suhu = input("masukan suhu dalam fahrenheit:")

#Rumus
K=get_kelvin(suhu)
C=get_celcius(suhu)
R=get_reamur(suhu)

#output
print(suhu + "Fahrenheit sama dengan")
print(str(K)+"Kelvin")
print(str(C)+"Celcius")
print(str(R)+"Reamur")



