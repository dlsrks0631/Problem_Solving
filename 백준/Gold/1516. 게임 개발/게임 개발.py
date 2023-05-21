import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

build_cost = [0] * (n+1)
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
result = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int,input().split()))
    
    build_cost[i] = data[0]
    index = 1
    
    while data[index] != -1:
        graph[data[index]].append(i)
        indegree[i] += 1
        index += 1

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
        
while queue:
    now = queue.popleft()
    for j in graph[now]:
        indegree[j] -= 1
        
        result[j] = max(result[j], result[now] + build_cost[now])
        if indegree[j] == 0:
            queue.append(j)

for k in range(1, n+1):
    print(build_cost[k] + result[k])