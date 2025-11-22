import math

# Input jari-jari dari pengguna
r = float(input("Masukkan jari-jari lingkaran: "))

# Hitung luas
luas = math.pi * r**2

# Hitung keliling
keliling = 2 * math.pi * r

# Tampilkan hasil
print(f"Luas lingkaran adalah: {luas:.2f}")
print(f"Keliling lingkaran adalah: {keliling:.2f}")
