import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

shark_level = 2
shark_x = 0
shark_y = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    distance = [[False] * n for _ in range(n)]

    queue = deque()
    queue.append((shark_x, shark_y))
    distance[shark_x][shark_y] = 0

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] is False and graph[nx][ny] <= shark_level:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                    
    return distance


def find(distance):
    min_distance = INF
    x, y = 0, 0
    
    for i in range(n):
        for j in range(n):
            if distance[i][j] is not False and 1 <= graph[i][j] < shark_level:
                if distance[i][j] < min_distance:
                    x, y = i, j
                    min_distance = distance[i][j]

    if min_distance == INF:
        return False
    else:
        return x, y, min_distance


result = 0
eat = 0

while True:
    data = find(bfs())

    if data is False:
        print(result)
        break
    
    else:
        shark_x, shark_y = data[0], data[1]
        result += data[2]

        graph[shark_x][shark_y] = 0
        eat += 1

        if eat == shark_level:
            shark_level += 1
            eat = 0