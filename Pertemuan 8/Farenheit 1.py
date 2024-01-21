print("Konversi Suhu Farenheit")

# Entry
suhu = input("Masukan Suhu Dalam Farenheit:")

# Rumus
C = 5/9 * (float(suhu) - 32)
R = 4/9 * (float(suhu) - 32)
K = 5/9 * (float (suhu) + 32) + 273

# output
print(suhu + "farenheit sama dengan")
print(str(C) + "Celcius")
print(str(R) + "Reamur")
print(str(K) + "Kelvin")