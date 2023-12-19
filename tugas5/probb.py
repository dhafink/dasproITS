def banyak_cara(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 3
    elif n == 5:
        return 5
    else:
        return banyak_cara(n-1) + banyak_cara(n-3) + banyak_cara(n-5)

S = int(input())
C = list(map(int, input().split()))
hasil = []

for i in C:
    newHasil = banyak_cara(i)
    hasil.append(newHasil)

for j in range(len(hasil)):
    print(f"SESI {j+1}: {hasil[j]}")