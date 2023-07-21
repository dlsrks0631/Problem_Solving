import sys

input = sys.stdin.readline

n = int(input())

graph = [[0] * 101 for _ in range(101)]

# direction 0, 1, 2, 3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    y, x, d, g = map(int, input().split())

    graph[x][y] = 1
    dragon_curve = []
    dragon_curve.append(d)

    for _ in range(g):
        for k in range(len(dragon_curve) - 1, -1, -1):
            dragon_curve.append((dragon_curve[k] + 1) % 4)

    for index in range(len(dragon_curve)):
        x += dx[dragon_curve[index]]
        y += dy[dragon_curve[index]]

        if 0 <= x < 101 and 0 <= y < 101:
            graph[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            result += 1

print(result)
