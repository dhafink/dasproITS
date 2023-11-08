f = [0 for i in range(0, 41)]
f[1] = 1
f[2] = 5
f[3] = 11
for j in range(4, 41):
    f[j] = f[j-1] + 4*f[j-2] + 2*f[j-3]
while(1):
    N = int(input())
    print(f[N])