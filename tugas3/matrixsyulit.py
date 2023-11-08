def matrix() : 
    a = int(input())
    matrix = []
    for i in range (a):
        x = input()
        matrix.append(list(x))

    atas = 0 #1
    bawah = a -1
    kiri = 0
    kanan = len(matrix[0]) - 1

    while atas <= bawah and kiri <= kanan:
        # Print atas
        for i in range(kiri, kanan + 1):
            print(matrix[atas][i], end='')
        atas += 1

        # Print kanan
        for i in range(atas, bawah + 1):
            print("",matrix[i][kanan], end='')
        kanan -= 1

        # Print bawah
        if atas <= bawah:
            for i in range(kanan, kiri -1, -1):
                print(matrix[bawah][i], end='')
            bawah -= 1

        # Print kiri
        if kiri <= kanan:
            for i in range(bawah, atas - 1, -1):
                print("",matrix[i][kiri], end='')
            kiri += 1
matrix()