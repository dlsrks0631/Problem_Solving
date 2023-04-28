import sys

input = sys.stdin.readline

s = [0, 1, 1]
n = int(input())

for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])

print(s[n])