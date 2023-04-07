from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y):
    n = len(graph)
    queue = deque([(x,y)])
    graph[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt


n = int(input())
graph = []
datas = []

for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            datas.append(bfs(graph, i, j))

datas.sort()
print(len(datas))
for k in range(len(datas)):
    print(datas[k])