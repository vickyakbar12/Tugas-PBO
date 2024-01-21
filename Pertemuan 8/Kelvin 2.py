print("Konversi Suhu Kelvin")

def get_reamur(suhu):
    R = 4/5 * (float(suhu) - 273)
    return R

def get_farenheit(suhu):
    F = 9/5 * (float (suhu) - 273) + 32
    return F

def get_celcius(suhu):
    C = float(suhu) - 273
    return C

# Entry
suhu = input("Masukkan suhu dalam kelvin:")

# rumus
R = get_reamur(suhu)
F = get_farenheit(suhu)
C = get_celcius(suhu)

# Output
print(suhu + " Kelvin sama dengan ")
print(str(R) + "Reamur")
print(str(F) + "Farenheit")
print(str(C) + "Celcius")