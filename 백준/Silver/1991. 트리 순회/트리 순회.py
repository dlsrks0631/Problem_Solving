import sys

input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left,right]
    
def PreOrder(now):
    if now == '.':
        return
    print(now, end = '')
    PreOrder(tree[now][0])
    PreOrder(tree[now][1])
    
def InOrder(now):
    if now == '.':
        return
    InOrder(tree[now][0])
    print(now, end = '')
    InOrder(tree[now][1])
    
def PostOrder(now):
    if now == '.':
        return
    PostOrder(tree[now][0])
    PostOrder(tree[now][1])
    print(now, end = '')
    
PreOrder('A')
print()
InOrder('A')
print()
PostOrder('A')

    