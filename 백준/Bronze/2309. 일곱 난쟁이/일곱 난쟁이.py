import itertools
import sys

input = sys.stdin.readline

data = [int(input()) for _ in range(9)]

for i in itertools.combinations(data, 7):  
    if sum(i) == 100: 
        for result in sorted(i):  
            print(result)
        break 