import sys

# n = 수 개수, m = 변경이 일어나는 횟수, k = 구간의 곱을 구하는 횟수
n,m,k = map(int,input().split())  

MOD = 1000000007
tree_height = 0
length = n

while length != 0:
    length //= 2
    tree_height += 1

tree_size = 2 ** (tree_height+1)
start_index = tree_size // 2 - 1
tree = [1] * (tree_size + 1)

for i in range(start_index + 1, start_index + n + 1):
    tree[i] = int(input())
    
# 리프노드를 제외한 거 채우기
def getIndexTree(i):
    while i != 1:
        tree[i // 2] = tree[i // 2] * tree[i] % MOD
        i -= 1

getIndexTree(tree_size - 1)
        
# 값 변경 함수
def change_value(index, change_val):
    tree[index] = change_val
    while index > 1:
        index //= 2
        tree[index] = tree[index*2] % MOD * tree[index*2 + 1] % MOD

def getMul(s,e):
    Mul = 1
    
    while s <= e:
        if s % 2 == 1:

            Mul = Mul * tree[s] % MOD
            s += 1
        if e % 2 == 0:
            Mul = Mul * tree[e] % MOD
            e -= 1
            
        s //= 2
        e //= 2
        
    return Mul
        

for _ in range(m+k):
    data, s, e = map(int,input().split())
    
    if data == 1:
        change_value(start_index+s,e)
        
    elif data == 2:
        s = s + start_index
        e = e + start_index
        
        print(getMul(s,e))
    
