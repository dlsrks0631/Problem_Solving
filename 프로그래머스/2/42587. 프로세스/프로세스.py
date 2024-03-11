from collections import deque

def solution(priorities, location):
    result = []

    n = len(priorities) 
    datas = deque()

    for i in range(n):
        datas.append((i, priorities[i]))
    priorities.sort()

    while datas:
        if datas[0][1] == priorities[-1]:
            result.append(datas.popleft()[0])
            priorities.pop()
        else:
            x,y = datas.popleft()
            datas.append((x,y))

    for j in range(n):
        if result[j] == location:
            return j + 1