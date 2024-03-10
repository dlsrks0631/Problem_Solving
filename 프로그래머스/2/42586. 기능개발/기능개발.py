import math

def solution(progresses, speeds):
    remain = []

    for i in range(len(progresses)):
        remain.append(math.ceil((100 - progresses[i]) / speeds[i]))

    result = [0] * (max(remain) + 1)

    day = 0
    for remain_day in remain:
        if day < remain_day:
            result[remain_day] += 1
            day = remain_day
        elif day >= remain_day:
            result[day] += 1

    answer = []
    for res in result:
        if res != 0:
            answer.append(res)
        
    return answer 