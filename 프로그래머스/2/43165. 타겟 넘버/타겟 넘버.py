def solution(numbers, target):
    result = [0]
    cnt = 0

    for num in numbers:
        temp = []

        for res in result:
            temp.append(res + num)
            temp.append(res - num)

        result = temp
    
    for res in result:
      if res == target:
        cnt += 1
    return cnt