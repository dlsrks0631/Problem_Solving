import sys

input = sys.stdin.readline

n = int(input())
datas = []
dp = [[-1] * (n+1) for _ in range(n+1)]

datas.append([0,0])

for _ in range(n):
    datas.append(list(map(int,input().split())))

def mat_chain(s, e):
    result = sys.maxsize # sys.maxsize > 현재 플랫폼에서 사용 가능한 가장 큰 정수

    if dp[s][e] != -1:
        return dp[s][e]
    if s == e:    # 행렬이 1개인 경우 0 반환
        return 0
    if s + 1 == e: # 행렬이 2개일 때
        return datas[s][0] * datas[s][1] * datas[e][1]
    
    for i in range(s,e): # 행렬이 3개 이상인 경우
        a = datas[s][0] * datas[i][1] * datas[e][1]  # 두 덩어리를 계산하는 연산
        result = min(result, a + mat_chain(s,i) + mat_chain(i+1, e))

    dp[s][e] = result
    return dp[s][e]

print(mat_chain(1, n))