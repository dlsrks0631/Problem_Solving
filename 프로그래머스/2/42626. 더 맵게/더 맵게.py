import heapq

def solution(scoville, K):
    heap = []

    for data in scoville:
        heapq.heappush(heap, data)

    answer = 0

    while len(heap) >= 2 and heap[0] < K:
        heap = spicy(heap)
        answer += 1
        
    if heap[0] >= K:
        return answer
    else:
        return -1

def spicy(scoville):
    x = heapq.heappop(scoville)
    y = heapq.heappop(scoville)
    heapq.heappush(scoville, x + 2 * y)

    return scoville