import sys

input = sys.stdin.readline

height, weight = map(int,input().split())

walls = list(map(int,input().split()))

result = 0
left = 0
right = weight - 1

left_max_height = walls[left]
right_max_height = walls[right]

result = 0

while left < right:
    left_max_height = max(left_max_height, walls[left])
    right_max_height = max(right_max_height, walls[right])

    if left_max_height >= right_max_height:
        result += right_max_height - walls[right]
        right -= 1
    else:
        result += left_max_height - walls[left]
        left += 1

print(result)
        
