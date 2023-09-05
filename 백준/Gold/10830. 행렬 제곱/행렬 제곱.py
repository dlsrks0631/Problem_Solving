def multiplication(array1, array2):
    n = len(array1)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += array1[i][k] * array2[k][j]
            result[i][j] %= 1000
    return result

def power(b, array):
    if b == 1:
        return array
    elif b == 2:
        return multiplication(array, array)
    tmp = power(b // 2, array)
    if b % 2 == 0:
        return multiplication(tmp, tmp)
    else:
        return multiplication(multiplication(tmp, tmp), array)


n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result = power(b, a)

for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()
