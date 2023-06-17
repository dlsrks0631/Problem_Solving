import sys

data = list(map(str, sys.stdin.readline().rstrip("\n")))
result = []

for i in range(1, len(data) - 1):
    for j in range(i + 1, len(data)):
        a = data[:i]
        b = data[i:j]
        c = data[j:] 

        a.reverse()
        b.reverse()
        c.reverse()

        result.append("".join(a + b + c))

print(min(result))