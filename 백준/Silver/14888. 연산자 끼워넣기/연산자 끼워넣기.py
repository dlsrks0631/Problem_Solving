import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

max_result = -sys.maxsize
min_result = sys.maxsize

nums = list(map(int,input().split()))
operators = list(map(int,input().split()))


def dfs(now, index):
    global max_result, min_result
    
    if index == n:
        max_result = max(max_result, now)
        min_result = min(min_result, now)
        return
    
    if operators[0] > 0:
        operators[0] -= 1
        dfs(now + nums[index], index + 1)
        operators[0] += 1
    
    if operators[1] > 0:
        operators[1] -= 1
        dfs(now - nums[index], index + 1)
        operators[1] += 1
        
    if operators[2] > 0:
        operators[2] -= 1
        dfs(now * nums[index], index + 1)
        operators[2] += 1
        
    if operators[3] > 0:
        operators[3] -= 1
        dfs(int(now / nums[index]), index + 1)
        operators[3] += 1
    
dfs(nums[0], 1)

print(max_result)
print(min_result)
