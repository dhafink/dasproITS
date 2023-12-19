from collections import deque
def bfs(grid, start, end):
    queue = deque([start])
    path = {start: None}
    while queue:
        point = queue.popleft()
        if point == end:
            break
        for neighbour in ((0,1), (0,-1), (1,0), (-1,0)):
            x, y = point[0] + neighbour[0], point[1] + neighbour[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#' and (x, y) not in path:
                queue.append((x, y))
                path[(x, y)] = point
    return path

def solve(grid):
    start, end = None, None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    if start is None or end is None:
        return "ada yang ga bener di start dan finishnya"
    path = bfs(grid, start, end)
    point = end
    while point != start:
        point = path[point]
        if point != start:
            grid[point[0]][point[1]] = 'x'
    return '\n'.join(''.join(row) for row in grid)


P, Q = map(int, input().split())
grid = []
for i in range(Q):
    newInput = list(input())
    grid.append(newInput)

print(solve(grid))