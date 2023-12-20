class Reamur:
    def __init__(self,suhu):
        self.suhu = suhu

    def get_reamur(self):
        val = self.suhu
        return val
    
    def get_fahrenheit(self):
        val = (9/4*float(suhu))+32
        return val
    
    def get_celcius(self):
        val = (5/4*float(suhu))
        return val
    
    def get_kelvin(self):
        val = (5/4*float(suhu))+273
        return val

suhu = input("masukan suhu dalam Reamur:")
r = Reamur(float(suhu))
val = r.get_reamur

#Rumus
F=r.get_fahrenheit()
C=r.get_celcius()
K=r.get_kelvin()

#output
print(str(val) + "Reamur sama dengan")
print(str(F)+"Fahrenheit")
print(str(C)+"Celcius")
print(str(K)+"Kelvin")
    