import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

for a in arr:
    if a in data:
        print(1)
    else:
        print(0)