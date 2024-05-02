def solution(n, k):
    answer = 0
    num = make_k(n,k)
    nums = list(str(num).split("0"))

    for x in nums:
        if x and isPrime(int(x)):
            answer += 1

    return answer

def make_k(n, k):
    result = ""
    if k == 10:
        return str(n)
    else:
        while n != 0:
            result += (str(n%k))
            n //= k
    

    return result[::-1]

def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(solution(437674,3))


