note = [-1 for i in range(39)]
note[0] = 9
note[1] = 10 
note[3] = 20

n = [0 for i in range(43)] 
n[2] = 1
n[3] = 0
n[4] = -1
n[5] = -2

for i in range(6,43):
    n[i] = n[i - 1] - 1

def fib(n):
    if(note[n] != -1):
        return note[n]
    else:
        if(n>0):
            note[n] = fib(n-1) + fib(n-2) + n[n]
        else:
            note[n] = 0
        return note[n]


n = int(input())
hasil = fib(n)
print(hasil)
