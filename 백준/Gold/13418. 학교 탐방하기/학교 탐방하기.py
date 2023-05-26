n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
edges = []
asc = 0
desc = 0

def make_set(a):
    parent[a] = a
    rank[a] = 0

for i in range(1, n + 1):
    make_set(i)
    
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1

for _ in range(m+1):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

edges.sort(key=lambda x: x[2])

for i in range(m+1):
    a, b, c = edges[i]
    if find(a) != find(b):
        union(a, b)
        if c == 0:
            asc += 1

edges.sort(key=lambda x: -x[2])

parent = [i for i in range(n + 1)]

for i in range(m+1):
    a, b, c = edges[i]
    if find(a) != find(b):
        union(a, b)
        if c == 0:
            desc += 1

result = asc ** 2 - desc ** 2
print(result)