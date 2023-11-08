# Membaca input jenis Batu Faktorial
n = int(input())

# Menghitung faktorial dari n
faktorial = 1
for i in range(1, n + 1):
    faktorial *= i

karakter = 0
while faktorial % 10 == 0:
    karakter += 1
    faktorial //= 10

# Memeriksa apakah harus menukarkan Batu Faktorial
if karakter % 4 == 0:
    print(karakter)
    print("Tuker dulu Rink!")
else:
    print(karakter)
    print("Gas pol rem blong, Rink!")