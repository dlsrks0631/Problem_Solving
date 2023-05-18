import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
start = int(input())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,cost = map(int,input().split())
    graph[s].append((e,cost))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
        
    
