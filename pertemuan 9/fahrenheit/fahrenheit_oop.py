class Fahrenheit:
    def __init__(self,suhu):
        self.suhu = suhu

    def get_fahrenheit(self):
        val = self.suhu
        return val
    
    def get_kelvin(self):
        val = (5/9*float(suhu)-32)+273   
        return val
    
    def get_celcius(self):
        val = (5/9*float(suhu)-32)
        return val
    
    def get_reamur(self):
        val = (4/9*float(suhu)-32)
        return val

suhu = input("masukan suhu dalam Fahrenheit:")
f = Fahrenheit(float(suhu))
val = f.get_fahrenheit

#Rumus
K=f.get_kelvin()
C=f.get_celcius()
R=f.get_reamur()

#output
print(str(val) + "Fahrenheit sama dengan")
print(str(K)+"Kelvin")
print(str(C)+"Celcius")
print(str(R)+"Reamur")
    