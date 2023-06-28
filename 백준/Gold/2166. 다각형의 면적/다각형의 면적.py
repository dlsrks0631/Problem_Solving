import sys

input = sys.stdin.readline

n = int(input())
result = 0

x = []
y = []

for i in range(n):
    x1,y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
    
x.append(x[0])
y.append(y[0])

for i in range(n):
    result += (x[i] * y[i+1]) - (x[i+1] * y[i])
    
print(round(abs(result/2), 1))