import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())
convey = deque(list(map(int,input().split())))
robot = deque([0] * n)
result = 0

while True:
    convey.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and convey[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                convey[i+1] -= 1
        robot[-1] = 0
    if robot[0] == 0 and convey[0]>=1:
        robot[0] = 1
        convey[0] -= 1
    result += 1
    
    if convey.count(0) >= k:
        break

print(result)