import sys

input = sys.stdin.readline

n = input().rstrip()

if n == n[::-1]:
    print(1)
else:
    print(0)
