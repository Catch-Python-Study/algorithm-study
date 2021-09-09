import math
n, k = map(int, input().split())
arr = list(map(int,input().split()))

print(math.ceil((n-1)/(k-1)))