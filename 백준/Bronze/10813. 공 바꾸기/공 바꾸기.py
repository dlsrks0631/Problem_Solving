n,m = map(int, input().split())

datas = [i for i in range(1,n+1)]

for i in range(m):
    i,j = map(int, input().split())
    datas[i-1], datas[j-1] = datas[j-1], datas[i-1]

for i in range(n):
    print(datas[i], end = ' ')