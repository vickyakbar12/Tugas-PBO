class Farenheit:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def get_farenheit(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = 5/9 * (self.suhu - 32)
        return val
    
    def get_reamur(self):
        val = 4/9 * (self.suhu - 32)
        return val
    
    def get_kelvin(self):
        val = 5/9 * (self.suhu + 32) + 273
        return val
    
suhu = input("Masukan suhu dalam farenheit:")
F = Farenheit(float(suhu))
val = F.get_farenheit()

C = F.get_celcius()
R = F.get_reamur()
K = F.get_kelvin()

print(str(val) + "Farenheit sama dengan:")
print(str(C) + "Celcius")    
print(str(R) + "Reamur")
print(str(K) + "Kelvin")