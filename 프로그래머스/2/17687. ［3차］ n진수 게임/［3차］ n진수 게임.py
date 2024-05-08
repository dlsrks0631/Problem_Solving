def convert_number(n, base):
    # 16진수까지가 범위이므로
    result = ""
    temp = "0123456789ABCDEF"

    while n > 0:
        r = n % base
        result = temp[r] + result
        n //= base

    return result

def solution(n, t, m, p):
    answer = ''

    num = 0
    while True:
        answer += convert_number(num, n)

        if len(answer) >= t * m:
            answer = answer[:t*m]
            return answer[p-1:t * m:m]
        num += 1