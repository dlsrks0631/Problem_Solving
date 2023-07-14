import sys

input = sys.stdin.readline

# 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0] 

dice = [0] * 6

# 동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4
def east():
    temp = dice[1]
    dice[1] = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = temp

def west():
    temp = dice[4]
    dice[4] = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = temp

def north():
    temp = dice[3]
    dice[3] = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = temp

def south():
    temp = dice[5]
    dice[5] = dice[2]
    dice[2] = dice[0]
    dice[0] = dice[3]
    dice[3] = temp
    
n,m,x,y,k = map(int,input().split())

datas = []

for _ in range(n):
    datas.append(list(map(int,input().split())))
    
moves = list(map(int,input().split()))

for i in moves:
    if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
        x += dx[i]
        y += dy[i]
        
        if i == 1:
            east()
        elif i == 2:
            west()
        elif i == 3:
            north()
        else:
            south()
            
        if datas[x][y] == 0:
            datas[x][y] = dice[0]
        else:
            dice[0] = datas[x][y]
            datas[x][y] = 0
    
        print(dice[5])



