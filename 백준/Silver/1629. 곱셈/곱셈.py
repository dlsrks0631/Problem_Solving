import sys

input = sys.stdin.readline

a,b,c = map(int,input().split())

def power(a,b):
    if b == 1:
        return a % c
    else:
        temp = power(a, b // 2)
        if b % 2 == 0:
            return temp ** 2 % c
        else:
            return temp ** 2 * a % c

print(power(a,b))