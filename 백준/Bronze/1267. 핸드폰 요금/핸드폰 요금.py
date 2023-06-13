N = int(input())
datas = list(map(int, input().split()))

y = 0
m = 0

for data in datas:
    y += (data//30 + 1) * 10
    m += (data//60 + 1) * 15
if m == y:
    print("Y M", m)
elif m < y:
    print("M", m)
else:
    print("Y", y)