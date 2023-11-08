#membuat input
n = int(input())
s = map(int,input().split())
angka = 0 
#mengubah s input menjadi bin
for i in s:
    bin_angka = bin(i)
    x = bin_angka.count("1")
    angka += x # menambah banyak jumlah "1" dalam loop
# print(bin_angka)
print(angka)