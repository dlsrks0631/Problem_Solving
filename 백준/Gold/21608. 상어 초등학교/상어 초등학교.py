import sys

input = sys.stdin.readline

love = {}

n = int(input())
room = [[0] * n for _ in range(n)]
sequence = []

for _ in range(n**2):
    data = list(map(int, input().split()))
    sequence.append(data[0])
    love[data[0]] = data[1:]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for seq in sequence:
    temp_list = []
    for i in range(n):
        for j in range(n):
            love_number = 0
            empty_number = 0
            if room[i][j] != 0:
                continue
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if room[nx][ny] in love[seq]:
                        love_number += 1
                    elif room[nx][ny] == 0:
                        empty_number += 1       
            
            temp_list.append((love_number, empty_number, i, j))
    temp_list.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    room[temp_list[0][2]][temp_list[0][3]] = seq

result = 0
for x in range(n):
    for y in range(n):
        satisfied = 0
        for dr in range(4):
            nx = x + dx[dr]
            ny = y + dy[dr]
            
            if 0 <= nx < n and 0 <= ny < n:
                if room[nx][ny] in love[room[x][y]]:
                    satisfied += 1
        
        result += int(10 ** (satisfied - 1))

print(result)