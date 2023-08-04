import sys

input = sys.stdin.readline

for _ in range(3):
    data = list(map(int, input().split()))
    
    if data.count(0) == 1:
        print("A")
        
    elif data.count(0) == 2:
        print("B")
        
    elif data.count(0) == 3:
        print("C")   
        
    elif data.count(0) == 4:
        print("D")
        
    else:
        print("E") 