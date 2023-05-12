n = int(input())

datas = []

for i in range(n):
    data = int(input())
    if data == 0:
        datas.pop()
    else:
        datas.append(data)
        
print(sum(datas))