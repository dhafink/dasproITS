def flood_fill(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return 0
    
    matrix[i][j] = 0
    size = 1

    size += flood_fill(matrix, i+1, j)
    size += flood_fill(matrix, i-1, j)
    size += flood_fill(matrix, i, j+1)
    size += flood_fill(matrix, i, j-1)

    return size

jumlahPulau = []
pulau = []

N, M = map(int, input().split())

for i in range(N):
    newInput = list(map(int, input().split()))
    pulau.append(newInput)

for i in range(len(pulau)):
    for j in range(len(pulau[i])):
        if pulau[i][j] == 1:
            jumlahPulau.append(flood_fill(pulau, i, j))

print(f"Banyak Pulau: {len(jumlahPulau)}")
print(f"Luas Pulau: {' '.join(str(x) for x in jumlahPulau)}")