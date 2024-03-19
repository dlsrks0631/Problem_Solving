def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    for winner, loser in results:
        graph[winner][loser] = 1
        graph[loser][winner] = -1
    
    # 이기면 1 지면 -1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                for k in range(1, n+1):
                    if graph[j][k] == 1:
                        graph[i][k] = 1

            elif graph[i][j] == -1:
                for k in range(1, n+1):
                    if graph[j][k] == -1:
                        graph[i][k] = -1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                for k in range(1, n+1):
                    if graph[j][k] == 1:
                        graph[i][k] = 1

            elif graph[i][j] == -1:
                for k in range(1, n+1):
                    if graph[j][k] == -1:
                        graph[i][k] = -1

    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if i != j and graph[i][j] != 0:
                count += 1

        if count == n - 1:
            answer += 1 

    return answer