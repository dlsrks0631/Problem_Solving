from collections import deque

def solution(queue1, queue2):
    deq1 = deque(queue1)
    deq2 = deque(queue2)

    sum1 = sum(deq1)
    sum2 = sum(deq2)

    result = 0

    while True:
        if sum1 > sum2:
            pop1 = deq1.popleft()
            sum2 += pop1
            sum1 -= pop1
            deq2.append(pop1)
            result += 1
        
        if sum1 < sum2:
            pop2 = deq2.popleft()
            sum1 += pop2
            sum2 -= pop2
            deq1.append(pop2)
            result += 1
        
        if sum1 == sum2:
            return result
        
        if result == len(deq1) * 3:
            return -1
        
    return result


print(solution([3,2,7,2], [4,6,5,1]))
print(solution([1, 10, 1, 2],[1, 2, 1, 2]))
print(solution([1, 1], [1,5]))
'''
[3,2,7,2] -> 14
[4,6,5,1] -> 16

둘 중 15로 맞춰야됨.

[1,2,1,2] -> 6
[1,10,1,2] -> 14

'''