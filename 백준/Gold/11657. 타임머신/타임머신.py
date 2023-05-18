import sys

INF = sys.maxsize
input = sys.stdin.readline

n,m = map(int,input().split())

edges = []
distance = [INF] * (n+1)

for _ in range(m):
    s,e,cost = map(int,input().split())
    edges.append((s,e,cost))
    
distance[1] = 0

# 시작점이 무한대가 아니고 D[e] > D[s] + w일 경우에 업데이트
for _ in range(n-1):
    for s,e,cost in edges:
        if distance[s] != INF and distance[e] > distance[s] + cost:
            distance[e] = distance[s] + cost
            
# 음수 사이클 확인
Minus_Cycle = False

for s,e,cost in edges:
    if distance[s] != INF and distance[e] > distance[s] + cost:
        Minus_Cycle = True
        
if Minus_Cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
            
    
    

