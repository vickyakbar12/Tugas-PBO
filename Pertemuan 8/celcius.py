# File-1 (celcius.py)
class Celcius:
  def __init__(self, suhu):
    self.suhu = suhu

  def get_celcius(self):
    val = self.suhu
    return val
    
  def get_fahrenheit(self):
    val = (9/5 * self.suhu) + 32
    return val
  
  def get_reamur(self):
    val = (4/5 * self.suhu) 
    return val
  
  def get_kelvin(self):
    val = self.suhu + 273
    return val