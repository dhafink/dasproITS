def hufi():
    #membuat batasan
    batas = int(input())
    for num in range(batas):
        n = input()
        #membalik posisi input
        kebalikan = n[::-1]
        if n == kebalikan : 
            print("Mehas pasti suka !")
        else:
            print("Jangan ini, deh.")
hufi()