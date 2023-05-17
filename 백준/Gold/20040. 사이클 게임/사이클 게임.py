import sys

input = sys.stdin.readline

n,m = map(int,input().split())

parent = [i for i in range(n+1)]

result = 0

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
        
def union(a,b):
    a = find(a)
    b = find(b)
    
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a
    else:
        return
        
for i in range(m):
    a,b = map(int,input().split())
    
    if find(a) == find(b):
        result = i+1
        break

    union(a,b)
        
print(result)    


