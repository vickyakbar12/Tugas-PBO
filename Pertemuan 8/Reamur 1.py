print("Konversi Suhu Reamur")

# Entry
suhu = input("Masukan Suhu Dalam Reamur:")

# Rumus
C = 5/4 * float(suhu)
F = (9/4 * float(suhu)) + 32
K = 5/4 * float (suhu) + 273

# output
print(suhu + "reamur sama dengan")
print(str(C) + "Celcius")
print(str(F) + "Farenheit")
print(str(K) + "Kelvin")