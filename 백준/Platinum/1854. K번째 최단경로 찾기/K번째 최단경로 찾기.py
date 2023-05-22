import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [[INF] * (k) for _ in range(n+1)]

for _ in range(m):
    s,e,cost = map(int,input().split())
    graph[s].append((e,cost))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start][0] = 0
    
    while q:
        dist,now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]][k-1] > cost:
                distance[i[0]][k-1] = cost
                distance[i[0]].sort()
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(1)

for i in range(1, n+1):
    if distance[i][k-1]== INF:
        print(-1)
    else:
        print(distance[i][k-1])