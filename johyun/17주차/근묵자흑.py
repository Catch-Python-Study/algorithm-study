import sys
import math
sys.stdin = open("input.txt", "r")
#	8 3
#	7 3 1 8 4 6 2 5  가 인풋값이다.


n,k = map(int, sys.stdin.readline().split())
listt = list(map(int, sys.stdin.readline().split()))

newlist = sorted(listt)
# n=n-k 를 사용하면 되지 않을까?

# for i in range(k):
#
# for i in range(n):
mini = newlist[0]
newlist[:k] = mini
print(newlist)

