n = int(input())
datas = []

for _ in range(n):
    datas.append(int(input()))
    
datas.sort()

answers = []
for data in datas:
    answers.append(data*n)
    n -= 1
    
print(max(answers))