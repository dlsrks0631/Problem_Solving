def solution(str1, str2):
    result = [] # 합집합
    result2 = [] # 교집합

    data1 = split(str1)
    data2 = split(str2)

    print(data1)
    print(data2)

    for d1 in data1:
        if d1 not in data2:
            result.append(d1)
        elif d1 in data2 and d1 not in result:
            for _ in range(max(data1.count(d1), data2.count(d1))):
                result.append(d1)

    for d2 in data2:
        if d2 not in result:
            for _ in range(data2.count(d2)):
                result.append(d2)

    for d1 in data1:
        if d1 in data2 and d1 not in result2:
            for _ in range(min(data1.count(d1), data2.count(d1))):
                result2.append(d1)

    if len(result) == 0:
        return 65536
    
    if len(result2) == 0 and len(result) != 0:
        return 0
    
    print(result)
    print(result2)
    # return result2, result
    return int(len(result2) / len(result) * 65536)

# 2개씩 문자 쪼개기
def split(datas):
    result = []

    for i in range(1, len(datas)):
        if datas[i-1].isalpha() and datas[i].isalpha():
            split_data = datas[i-1].upper() + datas[i].upper()
            result.append(split_data)

    return result


# print(solution("FRANCE", "french"))
# print(solution("handshake","shake hands"))
# print(solution("aa1+aa2","AAAA12"))
# print(solution("E=M*C^2", "E=M*C^2"))
print(solution("BAAAA", "AAA"))

str1 = 'abcccc'
str2 = 'cccdefff'
print(solution(str1, str2))

