import sys
import math
sys.stdin = open("input.txt", "r")
n,k = map(int, sys.stdin.readline().split())
listt = list(map(int, sys.stdin.readline().split()))

newlist = sorted(listt)
print(type(k),k, type(newlist))
# n=n-k 를 사용하면 되지 않을까?

mini = newlist[0]
newlist[:k] = mini
# print(newlist)
cnt=1
for i in range(n):
    idx = i
    newlist[i:n:k] = mini
    cnt+=1



