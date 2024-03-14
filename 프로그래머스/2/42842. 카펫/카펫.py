def solution(brown, yellow):
    total = brown + yellow

    lst = getDivision(total)
    print(lst)

    for height, width in lst:
        if (height - 2) * (width - 2) >= yellow:
            return ([width, height])


def getDivision(number):
    result = []

    for i in range(1, int(number ** 1/2) + 1):
        if number % i == 0:
            result.append((i, number // i))
    
    return result[0:len(result)//2 + 1]