from itertools import permutations

def solution(numbers):
    datas = []
    for num in numbers:
        datas.append(num)


    lst = set()
    for r in range(1, len(datas) + 1):
        perms = permutations(datas, r)
        for perm in perms:
            lst.add(int(''.join(map(str,perm))))

    answer = 0
    for ll in lst:
        if isPrime(ll):
            answer += 1
    
    return answer

def isPrime(number):
    if number == 1 or number == 0:
        return False
    
    for i in range(2, int(number ** 1/2) + 1):
        if number % i == 0:
            return False

    return True            
