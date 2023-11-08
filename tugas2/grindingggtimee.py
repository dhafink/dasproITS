n = int(input())

Abyss = n // 10
Hilichurl = 0
Slime = 0

n = n % 10
if 8 < n >= 10:
    n -= 10
    Abyss += 1
elif 6 < n<= 8:
    n -= 8
    Hilichurl += 1
else :
    n -= 6
    Slime += 1

total_damage = Slime * 3 + Hilichurl * 4 + Abyss * 5
print(total_damage)
print(Slime)
print(Hilichurl)
print(Abyss)