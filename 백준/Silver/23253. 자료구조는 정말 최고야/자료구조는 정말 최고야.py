import sys

input = sys.stdin.readline

n,k = map(int,input().split())

for _ in range(k):
    input()
    datas = list(map(int,input().split()))

    if datas != sorted(datas, reverse=True):
        print("No")
        exit(0)

print("Yes")