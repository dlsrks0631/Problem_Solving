from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [0] * (n + 1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    def bfs():
        queue = deque([1])

        while queue:
            now = queue.popleft()

            for next_node in graph[now]:
                if next_node != 1 and distance[next_node] == 0: 
                    distance[next_node] = distance[now] + 1
                    queue.append(next_node)

    bfs()
    count = 0
    for dist in distance:
        if dist == max(distance):
            count += 1

    return count