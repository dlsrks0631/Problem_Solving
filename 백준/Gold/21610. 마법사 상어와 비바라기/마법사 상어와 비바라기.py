import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

dr = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

clouds = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]

for _ in range(m):
    direction, distance = map(int, input().split())
    new_clouds = []
    for cloud in clouds:
        # 구름 이동
        cloud_x = (cloud[0] + (dr[direction - 1][0] * distance)) % n
        cloud_y = (cloud[1] + (dr[direction - 1][1] * distance)) % n
        new_clouds.append((cloud_x, cloud_y))
        # 구름 이동 후 물 1 추가
        data[cloud_x][cloud_y] += 1

    # 대각선 확인
    for cloud in new_clouds:
        for j in {(-1, -1), (-1, 1), (1, -1), (1, 1)}:
            if 0 <= cloud[0] + j[0] < n and 0 <= cloud[1] + j[1] < n:
                if data[cloud[0] + j[0]][cloud[1] + j[1]] > 0:
                    data[cloud[0]][cloud[1]] += 1

    clouds = []
    for x in range(n):
        for y in range(n):
            if data[x][y] >= 2 and (x, y) not in new_clouds:
                clouds.append((x, y))
                data[x][y] -= 2

result = 0
for x in range(n):
    for y in range(n):
        result += data[x][y]

print(result)
