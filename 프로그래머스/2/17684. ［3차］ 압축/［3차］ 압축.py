def solution(msg):
    messages = {chr(65+i) : i+1 for i in range(26)}
    
    index = 0
    temp = ''
    answer = []
    current = 27
    
    while index < len(msg):
        temp += msg[index]
        if temp in messages:
            index += 1
        else:
            messages[temp] = current
            current += 1
            answer.append(messages[temp[:-1]])
            temp = ''

    answer.append(messages[temp])

    return answer

st = "KAKAO"
print(solution(st))