import heapq

def solution(jobs):
    total = 0
    now = 0 # 현재 시간
    count = 0
    last_time = -1 # 마지막 완료 시간
    heap = []

    while count < len(jobs):
        for job in jobs:
            if last_time < job[0] <= now:  # 마지막 완료 시간 < 시작 시간 <= 현재 시간이면 처리시간 기준으로 (처리시간, 시작시간) push
                heapq.heappush(heap, [job[1], job[0]])
            
        if heap:
            run_time, start_time= heapq.heappop(heap)
            last_time = now
            now += run_time
            total += (now - start_time)
            count += 1

        else:
            now += 1

    return total // len(jobs)


print(solution([[0,3], [1,9], [2,6]]))