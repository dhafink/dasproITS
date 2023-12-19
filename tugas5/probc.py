def dfs(matrix, pos, path=[]):
    x, y = pos
    if pos in path:
        return None
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] == 0:
        return None
    
    path.append(pos)

    if pos == (len(matrix)-1, len(matrix[0])-1):
        return path
    result = dfs(matrix, (x+1, y), path) or dfs(matrix, (x, y+1), path)
    if result is None:
        path.remove(pos)

    return result

def solve(matrix):
    result = dfs(matrix, (0, 0))
    if result is None:
        return "Hari ini Bunda nggak masak"
    
    new_matrix = [[0]*len(matrix[0]) for _ in range(len(matrix))]

    for x, y in result:
        new_matrix[x][y] = 1

    return new_matrix


N, M = map(int, input().split())
matrix = []

for i in range(M):
    newInput = list(map(int, input().split()))
    matrix.append(newInput)

solved = solve(matrix)

for i in range(len(solved)):
    for j in range(len(solved[0])):
        print(solved[i][j], end=" ")
    print()