import sys

input = sys.stdin.readline

n = int(input())

# DP테이블 초기화
D = [0] * (n+1)
D[1] = 0    # 1일 때는 연산이 필요하지 않음

# 바텀-업 방식
for i in range(2, n+1):
    D[i] = D[i-1] + 1
    if i % 3 == 0:
        D[i] = min(D[i], D[i//3] + 1)
    if i % 2 == 0:
        D[i] = min(D[i], D[i//2] + 1)

print(D[n])