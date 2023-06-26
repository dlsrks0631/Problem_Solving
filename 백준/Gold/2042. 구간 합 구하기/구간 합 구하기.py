import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

tree_h = 0 # 트리의 높이
length = n # 길이


# 트리의 높이를 구하기
while length != 0:
    length //= 2
    tree_h += 1
    
tree_size = 2**(tree_h+1)
leaf_node_start = tree_size // 2 - 1
tree = [0] * (tree_size + 1)

# 데이터 리프노드에 저장
for i in range(leaf_node_start + 1, leaf_node_start + n + 1):
    tree[i] = int(input())
    
# 남은 트리 생성 -> 부모 노드 채워나가기
def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1
        
setTree(tree_size - 1)        

# 부모 노드로 가면서 자기 값에 차이값만 더해주면 됨
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2

# 구간 합 구하기
def getSum(s, e):
    partSum = 0
    
    # 시작이 종료와 교차될 때까지
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
        if e % 2 == 0:
            partSum += tree[e]
        
        s = (s + 1) // 2
        e = (e - 1) // 2
        
    return partSum

for _ in range(m+k):
    data, s, e = map(int,input().split())
    if data == 1:
        changeVal(leaf_node_start + s, e)
    elif data == 2:
        s = s + leaf_node_start
        e = e + leaf_node_start
        
        print(getSum(s,e))
        
