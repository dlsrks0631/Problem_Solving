import sys
import math

input = sys.stdin.readline

h,w,n,m = map(int,input().split())

y = math.ceil(h/(n+1)) 
x = math.ceil(w/(m+1))

print(x*y)