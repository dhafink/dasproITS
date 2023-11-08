memo = [-1 for x in range(39)]
memo[0] = 9
memo[1] = 10
memo[2] = 20

x = [0 for x in range(43)]
x[2] = 1
x[3] = 0
x[4] = -1
x[5] = -2
for i in range(6,43):
    x[i] = x[i-1] - 1
def fib(n):
    if(memo[n] != -1):
        return memo[n]
    else:
        if(n>0):
            memo[n] = fib(n-1) + fib(n-2) + x[n]
        else:
            memo[n] = 0
        return memo[n]
 
n = int(input())
hasil = fib(n)
print(hasil)