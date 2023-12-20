class Kelvin:
    def __init__(self,suhu):
        self.suhu = suhu

    def get_kelvin(self):
        val = self.suhu
        return val
    
    def get_fahrenheit(self):
        val = (9/5*float(suhu)-273)+32
        return val
    
    def get_celcius(self):
        val = (float(suhu))-273
        return val
    
    def get_reamur(self):
        val = (4/5*float(suhu)-273)
        return val

suhu = input("masukan suhu dalam kelvin:")
k = Kelvin(float(suhu))
val = k.get_kelvin

#Rumus
F=k.get_fahrenheit()
C=k.get_celcius()
R=k.get_reamur()

#output
print(str(val) + "Kelvin sama dengan")
print(str(F)+"Fahrenheit")
print(str(C)+"Celcius")
print(str(R)+"Reamur")
    