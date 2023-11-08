angka = int(input())
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

if angka >= 250000:
    a += angka // 250000
    angka %= 250000
if angka >= 100000:
    a += angka // 100000
    angka %= 100000
if angka >= 50000:
    a += angka // 50000
    angka %= 50000
if angka >= 20000:
    a += angka // 2000
    angka %= 2000
if angka >= 10000:
    a += angka // 10000
    angka %= 10000
if angka >= 5000:
    a += angka // 5000
    angka %= 5000

if angka >= 0:
    print("harganya jelek :(")
    
else :
    print(f'{a} lembar 250 ribuan')
    print(f'{b} lembar 100 ribuan')
    print(f'{c} lembar 50 ribuan')
    print(f'{d} lembar 20 ribuan')
    print(f'{e} lembar 10 ribuan')
    print(f'{f} lembar 5 ribuan')