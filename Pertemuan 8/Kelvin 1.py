print("Konversi Suhu Kelvin")

# Entry
suhu = input("Masukan Suhu Dalam Kelvin:")

# Rumus
R = 4/5 * (float(suhu) - 273)
F = 9/5 * (float (suhu) - 273) + 32
C = float(suhu) - 273

# output
print(suhu + "Kelvin sama dengan")
print(str(R) + "Reamur")
print(str(F) + "Farenheit")
print(str(C) + "Celcius")