from sys import stdin
from collections import deque

input = stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def find_next(lake, visited, queue):
    next_queue = deque()
    while queue:
        y, x = queue.popleft()
        if y == end_swan[0] and x == end_swan[1]:
            return True, None

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < row) or not (0 <= nx < column):
                continue

            if visited[ny][nx]:
                continue

            if lake[ny][nx] == 'X':
                next_queue.append((ny, nx))
            else:
                queue.append((ny, nx))
            visited[ny][nx] = True

    return False, next_queue



def melt_ice(ice_queue, lake):
    next_ice_queue = deque()
    while ice_queue:
        y, x = ice_queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < row) or not (0 <= nx < column):
                continue

            if lake[ny][nx] == 'X':
                lake[ny][nx] = '.'
                next_ice_queue.append((ny, nx))

    return next_ice_queue


row, column = map(int, input().split())
lake = [list(input().rstrip()) for _ in range(row)]

start_swan = None
end_swan = None
water = deque()

for r in range(row):
    for c in range(column):
        if lake[r][c] == '.' or lake[r][c] == 'L':
            water.append((r, c))
        if lake[r][c] == 'L':
            if start_swan is None:
                start_swan = (r, c)
            else:
                end_swan = (r, c)

result = -1
visited = [[False] * column for _ in range(row)]
queue = deque()

queue.append(start_swan)
visited[start_swan[0]][start_swan[1]] = True

while True:
    result += 1
    found, queue = find_next(lake, visited, queue)
    if found:
        break
    water = melt_ice(water, lake)

print(result)
