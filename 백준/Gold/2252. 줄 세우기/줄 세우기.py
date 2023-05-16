import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
data = [[] for _ in range(n+1)] # 인접리스트

indegree = [0] * (n+1) # 진입차수 리스트

for _ in range(m):
    s,e = map(int,input().split())
    data[s].append(e)
    indegree[e] += 1

queue = deque()

for j in range(1, n+1):
    if indegree[j] == 0:
        queue.append(j)

while queue:
    now = queue.popleft()
    print(now, end = ' ')
    for i in data[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

    