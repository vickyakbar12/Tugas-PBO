print("Konversi Suhu Celcius")

# Entry
suhu = input("Masukan Suhu Dalam Celcius:")

# Rumus
F = (9/5 * float(suhu)) + 32
R = (4/5 * float(suhu))
K = float (suhu) + 273

# output
print(suhu + "celcius sama dengan")
print(str(F) + "Farenheit")
print(str(R) + "Reamur")
print(str(K) + "Kelvin")