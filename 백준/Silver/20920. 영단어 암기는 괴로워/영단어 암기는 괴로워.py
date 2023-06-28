import sys

input = sys.stdin.readline

n, m = map(int, input().split())

datas = {}

for _ in range(n):
    data = input().rstrip()
    
    if len(data) >= m:
        if data not in datas:
            datas[data] = 1
            
        else:
            datas[data] += 1
            
datas = sorted(datas.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for a, b in datas:
    print(a)
