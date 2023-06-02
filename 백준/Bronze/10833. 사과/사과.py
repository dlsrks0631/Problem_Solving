N = int(input())
result = 0
for _ in range(N):
    A, B = map(int, input().split())
    result += B % A
    
print(result)