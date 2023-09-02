# 올바른 문자열인지 확인
def isproper(p):
    left_count = 0
    right_count = 0
    for i in p:
        if i == '(':
            left_count += 1
        else:
            if left_count == 0:
                return False
            left_count -= 1
    return True    

# 균형잡힌 문자열 index 반환
def properindex(p):
    left_count = 0
    for index in range(len(p)):
        if p[index] == '(':
            left_count += 1
        elif p[index] == ')':
            left_count -= 1
        
        if left_count == 0:
            return index



def solution(p):
    answer = ''

    # 빈 문자열인 경우
    if p == '':
        return answer
    
    index = properindex(p)
    u = p[:index+1]
    v = p[index+1:]
    
    if isproper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
        
    return answer


