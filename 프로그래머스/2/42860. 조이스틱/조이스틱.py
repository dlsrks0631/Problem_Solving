def solution(name):
    answer = 0
    n = len(name)
    for i in range(len(name)):
        if name[i] != 'A':
            answer += min((abs(ord(name[i]) - ord('A'))), 26 - abs(ord(name[i]) - ord('A')))

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move

    return answer