on = []
data = 0

for _ in range(4):
    a, b = map(int, input().split())
    data += b
    data -= a
    on.append(data)

print(max(on))