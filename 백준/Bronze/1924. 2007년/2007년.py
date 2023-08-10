import sys

input = sys.stdin.readline
x, y = map(int,input().split())

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
days = 0
 
for i in range(x-1):
    days = days + months[i]
days = (days + y) % 7
 
print(result[days])