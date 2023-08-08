import sys
from collections import deque

input = sys.stdin.readline

col, row = map(int, input().split())

graph = []

for _ in range(col):
    graph.append(list(input()))

for i in range(col):
    for j in range(row):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j
        elif graph[i][j] == 'O':
            x, y = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by))

    visited = []
    visited.append((rx, ry, bx, by))
    count = 0

    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if count > 10:
                print(-1)
                return
            if graph[rx][ry] == 'O':
                print(count)
                return
            for i in range(4):
                nx, ny = rx, ry
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if graph[nx][ny] == '#':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if graph[nx][ny] == 'O':
                        break
                    
                nx_b, ny_b = bx, by
                while True:
                    nx_b += dx[i]
                    ny_b += dy[i]

                    if graph[nx_b][ny_b] == '#':
                        nx_b -= dx[i]
                        ny_b -= dy[i]
                        break
                    if graph[nx_b][ny_b] == 'O':
                        break
                    
                if graph[nx_b][ny_b] == 'O':
                    continue
                
                if nx == nx_b and ny == ny_b:
                    if abs(nx - rx) + abs(ny - ry) > abs(nx_b - bx) + abs(ny_b - by):
                        nx -= dx[i]
                        ny -= dy[i]
                    else:
                        nx_b -= dx[i]
                        ny_b -= dy[i]
                        
                if (nx, ny, nx_b, ny_b) not in visited:
                    queue.append((nx, ny, nx_b, ny_b))
                    visited.append((nx, ny, nx_b, ny_b))
        count += 1
    print(-1)


bfs(rx, ry, bx, by)
