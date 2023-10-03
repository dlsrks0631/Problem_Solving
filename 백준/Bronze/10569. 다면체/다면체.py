import sys

input = sys.stdin.readline

for _ in range(int(input())):
    v,e = map(int, input().split())
    print(e - v + 2)