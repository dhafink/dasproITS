def gunuung(n):
    if n == 1:
        print("*") 
        return 
    if n == 2:
        print("**")
    else:
        gunuung(n - 2)
        print("*" * n)
        gunuung(n - 2)

n = int(input())
gunuung(n)
