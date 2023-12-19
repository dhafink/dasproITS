def Hitungcara(n, ular, memo): 
    if n == 100:
        return 1
    
    if (n, ular) in memo:
        return memo[(n, ular)]

    bnyk_car = 0
    for i in range(1, 7):
        if n + i != ular and n + i <= 100:
            bnyk_car += Hitungcara(n + i, ular, memo)

    memo[(n, ular)] = bnyk_car
    return bnyk_car

N, M = map(int, input().split())
memo_cara = {}
bynk_cr = Hitungcara(N, M, memo_cara)
print(f"Ada {memo_cara[(N, M)]} cara nih!")



# 99--->1
# 
# 98--->1 + (1)[99]
#   --->2

# 97 ---> 1 + (1 + 1) [98]
#     --->1 + (2) [98]
#     --->2 + (1) [99]
#     --->3

# 96  ---> 1 + (3) [97]
#     ---> 3 + (1) [99]
#     --->