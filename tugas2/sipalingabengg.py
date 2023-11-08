a,b = map(int, input().split())

if a % 2 != 0 and b % 2 == 0:
    print("Abeng")
if a % 2 != 0 and b % 2 != 0:
    print("Bahresi")
if a % 2 == 0 and b % 2 == 0:
    print("Bahresi")
if a % 2 == 0 and b % 2 != 0:
    print("Bahresi")