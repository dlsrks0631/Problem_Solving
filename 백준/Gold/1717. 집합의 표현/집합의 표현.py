import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

parent = [0] * (n+1)
rank = [0] * (n+1)

def make_set(a):
    parent[a] = a
    rank[a] = 0

for i in range(1,n+1):
    make_set(i)

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
        if rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1

for _ in range(m):
    data, a, b = map(int,input().split())

    if data == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
          
