# membuat input
batas = int(input())
n1,n2,n3 = map(int,input().split())
mulai = input()
# pengelompokan hari
hari = ['minggu','senin','selasa','rabu','kamis',"jumat",'sabtu']
# membuat KPK
if n1 > n2 and n3 : 
    higher = n1
elif n2 > n1 and n3 : 
    higher = n2
else : 
    higher = n3
nilai = higher
while 1:
    if higher % n1 == 0 and higher % n2 == 0 and higher % n3 == 0 :
        x = higher # hasil KPK
        # print(higher)
        break
    else:
        higher += nilai # akan terus bertambah sampai "n" % higher == 0
# menentukan index mulai
mulai_index= hari.index(mulai)
# menentukan hari temu
final_day_index = (mulai_index + x) % 7
final_day = hari[final_day_index]

print(final_day)