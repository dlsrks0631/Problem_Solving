import sys

input = sys.stdin.readline

INF = sys.maxsize
n,m = map(int,input().split())

tree_h = 0
length = n

while length != 0:
    length //= 2
    tree_h += 1
    
tree_size = 2 ** (tree_h + 1)
start_index = tree_size // 2 - 1
tree = [INF] * (tree_size + 1)

for i in range(start_index + 1, start_index + n + 1):
    tree[i] = int(input())

# 최솟값 인덱스 트리 생성
def setTree(i):
    while i != 1:
        if tree[i // 2] > tree[i]:
            tree[i // 2] = tree[i]
        i -= 1

setTree(tree_size - 1)

# 최솟값 계산 함수
def getMin(s,e):
    Min = INF
    while s <= e:
        if s % 2 == 1:
            Min = min(Min, tree[s])
            s += 1
            
        if e % 2 == 0:
            Min = min(Min, tree[e])
            e -= 1
            
        s //= 2
        e //= 2
    
    return Min

for _ in range(m):
    s, e = map(int,input().split())
    s = s + start_index
    e = e + start_index
    print(getMin(s,e))
    
            
            