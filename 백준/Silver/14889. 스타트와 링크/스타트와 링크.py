import sys
from itertools import combinations

n = int(input())
result = sys.maxsize

datas = []

for _ in range(n):
    datas.append(list(map(int,input().split())))

temp_list = [i for i in range(n)]
comb_list = list(combinations(temp_list, n//2))

for comb in comb_list:
    team_start = comb
    team_link = tuple(set(temp_list) - set(comb))
    start = 0
    link = 0
    
    for i,j in combinations(team_start, 2):
        start += datas[i][j] + datas[j][i]

    for k,l in combinations(team_link, 2):
        link += datas[k][l] + datas[l][k]
        
    result = min(abs(start - link), result)
    
print(result)

