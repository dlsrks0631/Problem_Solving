from collections import deque

def solution(begin, target, words):    
    if target not in words:
        return 0
    
    visited = [False] * len(words)

    def bfs():
        queue = deque([(begin, 0)])

        while queue:
            current, step = queue.popleft()

            if current == target:
                return step

            for word in words:
                count = 0
                for i in range(len(current)):
                    if current[i] != word[i]:
                        count += 1

                if count == 1:
                    queue.append((word, step + 1))

    answer = bfs()
    return answer