def copy_array(numlist, sizearray, destination, pos):
    for i in range(sizearray):
        destination[pos][i] = numlist[i]

def print_array(numlist, sizearray):
    for i in range(sizearray):
        print(numlist[i], end=' ')
    print()

def print_array_3d(numlist, sizearray, pos):
    for j in range(sizearray):
        print(numlist[pos][j], end=' ')
    print()

def pascal(numlist, sizearray, pos):
    if sizearray == 1:
        # print(numlist[0])
        pass
    else:
        pascallist = [0] * (sizearray - 1)
        for i in range(sizearray - 1):
            sum_val = numlist[i] + numlist[i + 1]
            pascallist[i] = sum_val

        copy_array(pascallist, sizearray - 1, hasilpascal, pos)
        pos += 1
        pascal(pascallist, sizearray - 1, pos)
        pos -= 1
        print_array_3d(hasilpascal, sizearray - 1, pos)

def pascal_full(numlist, sizearray):
    pascal(numlist, sizearray, 0)
    print_array(numlist, sizearray)

x = int(input())
numlist = list(map(int, input().split()))
hasilpascal = [[0] * 101 for k in range(101)]
pascal_full(numlist, x)