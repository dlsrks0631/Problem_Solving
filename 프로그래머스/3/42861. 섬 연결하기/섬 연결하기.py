def find_parent(parent, x):
    if parent[x] == x: 
        return x
    return find_parent(parent, parent[x])

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def iscycle(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a == b: return True
    return False

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [0] * n
    result = 0

    for i in range(n):
        parent[i] = i

    for start, end, cost in costs:
        if not iscycle(parent, start, end):
            union(parent, start, end)
            result += cost
    
    return result

