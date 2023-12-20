class Celcius:
    def __init__(self,suhu):
        self.suhu = suhu

    def get_celcius(self):
        val = self.suhu
        return val
    
    def get_fahrenheit(self):
        val = (9/5*float(suhu))+32
        return val
    
    def get_reamur(self):
        val = (4/5*float(suhu))
        return val
    
    def get_kelvin(self):
        val = self.suhu + 273
        return val

suhu = input("masukan suhu dalam celcius:")
c = Celcius(float(suhu))
val = c.get_celcius

#Rumus
F=c.get_fahrenheit()
R=c.get_reamur()
K=c.get_kelvin()

#output
print(str(val) + "celcius sama dengan")
print(str(F)+"Fahrenheit")
print(str(R)+"Reamur")
print(str(K)+"Kelvin")
    