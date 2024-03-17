def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0, numbers, target)
    return answer

def dfs(index, total, numbers, target):
    global answer
    # 탈출 조건
    if index == len(numbers):
        if total == target:
            answer += 1
        return
    
    # 현재 숫자를 더하거나 빼는 경우를 탐색
    dfs(index + 1, total + numbers[index], numbers, target)
    dfs(index + 1, total - numbers[index], numbers, target)