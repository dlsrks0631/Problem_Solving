import sys

input = sys.stdin.readline

n,m = map(int, input().split())

datas = [i for i in range(1,n+1)]

for i in range(m):
    i,j = map(int, input().split())
    temp = datas[i-1:j]
    temp.reverse()
    datas[i-1:j] = temp

for i in range(n):
    print(datas[i], end = ' ')