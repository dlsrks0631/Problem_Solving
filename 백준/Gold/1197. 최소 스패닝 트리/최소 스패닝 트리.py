import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)  # 정점 방문 처리

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))


def prim(weight, start):
    q = []
    heapq.heappush(q, (weight, start))
    result = 0  # 가중치의 합
    cnt = 0  # 간선의 개수

    while cnt < n:
        k, v = heapq.heappop(q)
        if visited[v]:
            continue
        visited[v] = True
        result += k
        cnt += 1
        for u, w in graph[v]:
            heapq.heappush(q, (w, u))
    return result


print(prim(0, 1))
