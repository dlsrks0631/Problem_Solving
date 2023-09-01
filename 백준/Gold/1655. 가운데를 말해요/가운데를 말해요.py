import sys
import heapq

input = sys.stdin.readline

n = int(input())

max_heap = []
min_heap = []

for i in range(n):
    data = int(input())
    
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -data)
    
    else:
        heapq.heappush(min_heap, data)
    
    if max_heap and min_heap and max_heap[0] * -1 > min_heap[0]:
        max_heap_pop = heapq.heappop(max_heap)
        min_heap_pop = heapq.heappop(min_heap)
        
        heapq.heappush(max_heap, min_heap_pop * -1)
        heapq.heappush(min_heap, max_heap_pop * -1) 
    
    print(max_heap[0] * -1)
        

