def hitung_maksimum_alumunium(x, y, matriks_alumunium, s):
    maksimum_alumunium = 0

    for i in range(x - s + 1):
        for j in range(y - s + 1):
            total_alumunium = 0
            for k in range(s):
                for l in range(s):
                    total_alumunium += matriks_alumunium[i + k][j + l]
            maksimum_alumunium = max(maksimum_alumunium, total_alumunium)

    return maksimum_alumunium

# Membaca input dari pengguna
x, y = map(int, input().split())
matriks_alumunium = []
for _ in range(y):
    baris = list(map(int, input().split()))
    matriks_alumunium.append(baris)
s = int(input())

# Menghitung jumlah maksimum alumunium dalam sekali gali
hasil = hitung_maksimum_alumunium(x, y, matriks_alumunium, s)

# Menampilkan hasil
print(hasil)
