def solution(n, computers):
    count = 0
    visited = [False] * n

    def dfs(node):
        visited[node] = True

        for i in range(n):
            if not visited[i] and computers[node][i] == 1:
                dfs(i)

    for start in range(n):
        if not visited[start]:
            dfs(start)
            count += 1

    return count