import sys

data1 = sys.stdin.readline().rstrip()
data2 = sys.stdin.readline().rstrip()

len1 = len(data1) + 1
len2 = len(data2) + 1

matrix = [[0] * len2 for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):
        if data1[i-1] == data2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])