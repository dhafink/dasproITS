tahun = int(input())

hari = tahun - 1900
tahun_kabisat = (hari-1)//4 + 1
tahun_kabisat -= ((hari-1)//100+1)
tahun_kabisat =+ (tahun - 1601)//400

hari += tahun_kabisat
hari %= 7

if(hari == 0):
    print("minggu")
elif(hari == 1):
    print("senin")
elif(hari == 2):
    print("selasa")
elif(hari == 3):
    print("rabu")
elif(hari == 4):
    print("kamis")
elif(hari == 5):
    print("jumat")
elif(hari == 6):
    print("sabtu")