import sys

input = sys.stdin.readline

n = int(input())
datas = list(map(int,input().split()))

# 오른쪽에서 index를 포함한 최대 연속 합 구하기
L = [0] * n
L[0] = datas[0]
result = L[0]

for i in range(1, n):
    L[i] = max(datas[i], L[i-1] + datas[i])
    result = max(result, L[i])

# 왼쪽으로 index를 포함한 최대 연속 합 구하기
R = [0] * n
R[-1] = datas[-1]

for j in range(n-2, -1, -1):
    R[j] = max(datas[j], R[j+1] + datas[j])

# L[i-1] + R[i+1] 2개의 구간 합 리스트를 더하면 i번째 값을 제거한 효과
for k in range(1, n-1):
    tmp = L[k-1] + R[k+1]
    result = max(result, tmp)

print(result)