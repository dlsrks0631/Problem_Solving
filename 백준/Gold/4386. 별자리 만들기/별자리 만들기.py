import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
data = []
parent = [i for i in range(n+1)]

for _ in range(n):
    x,y = map(float,input().split())
    data.append((x,y))

distance = []

def set_distance(x1, y1, x2, y2):
    result1 = (x2-x1)**2 + (y2-y1)**2
    result2 = result1**(1/2)
    
    return result2
    
for i in range(n):
    for j in range(n):
        distance.append((i+1,j+1,set_distance(data[i][0], data[i][1], data[j][0], data[j][1])))

distance.sort(key = lambda x : x[2])

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a

result = 0
for a,b,cost in distance:
    if find(a) != find(b):
        union(a,b)
        result += cost
        
print(round(result,2))
            