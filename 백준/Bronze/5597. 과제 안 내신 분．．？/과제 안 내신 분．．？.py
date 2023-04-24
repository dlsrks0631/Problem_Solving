
datas = [i for i in range(1, 31)]

for _ in range(28):
    data = int(input())
    datas.remove(data)
    
print(min(datas))
print(max(datas))