import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

datas = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int,input().split())
    datas[start].append((end, cost))

start, end = map(int,input().split())

distance = [sys.maxsize] * (n+1)
def dijkstra(start):
    hq = []
    distance[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        dist, now = heapq.heappop(hq)

        if distance[now] < dist:
            continue

        for i in datas[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(hq, (dist + i[1], i[0]))

dijkstra(start)

print(distance[end])









    
