import sys

input = sys.stdin.readline

datas = list(''.join(map(str, input().rstrip())))

temp_data = []
temp = 1
result = 0
for i in range(len(datas)):
    if datas[i] == '(':
        temp_data.append(datas[i])
        temp *= 2
    elif datas[i] == '[':
        temp_data.append(datas[i])
        temp *= 3
    elif datas[i] == ')':
        if datas[i-1] == '(':
            result += temp
        if not temp_data or temp_data[-1] != '(':
            result = 0
            break

        temp_data.pop()
        temp //= 2
    elif datas[i] == ']':
        if datas[i-1] == '[':
            result += temp
        if not temp_data or temp_data[-1] != '[':
            result = 0
            break

        temp_data.pop()
        temp //= 3

if temp_data:
    result = 0


print(result)

        


