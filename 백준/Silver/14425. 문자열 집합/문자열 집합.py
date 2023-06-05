import sys

input = sys.stdin.readline

count = 0
n,m = map(int,input().split())
text = set([input() for _ in range(n)])

for i in range(m):
    data = input()
    if data in text:
        count += 1

print(count)