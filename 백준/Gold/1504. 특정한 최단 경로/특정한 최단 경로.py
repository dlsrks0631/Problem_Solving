import sys
import heapq

input = sys.stdin.readline

n,e = map(int,input().split())

datas = [[] for _ in range(n+1)]

for _ in range(e):
    start, end, cost = map(int,input().split())

    datas[start].append((end, cost))
    datas[end].append((start, cost))

a,b = map(int, input().split())


def dijkstra(start):
    q = []
    distance = [sys.maxsize] * (n+1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in datas[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

distance = dijkstra(1)
distance_a = dijkstra(a)
distance_b = dijkstra(b)

cost_a = distance[a] + distance_a[b] + distance_b[n]
cost_b = distance[b] + distance_b[a] + distance_a[n]
result = min(cost_a, cost_b)

if result < sys.maxsize:
    print(result)
else:
    print(-1)
