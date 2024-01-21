class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def get_reamur(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = 5/4 * self.suhu
        return val
    
    def get_farenheit(self):
        val = (9/4 * self.suhu) + 32
        return val
    
    def get_kelvin(self):
        val = 5/4 * self.suhu + 273
        return val
    
suhu = input("Masukan suhu dalam reamur:")
R = Reamur(float(suhu))
val = R.get_reamur()

C = R.get_celcius()
F = R.get_farenheit()
K = R.get_kelvin()

print(str(val) + "Reamur sama dengan:")
print(str(C) + "Celcius")    
print(str(F) + "Farenheit")
print(str(K) + "Kelvin")