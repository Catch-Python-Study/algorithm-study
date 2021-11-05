import sys
sys.stdin = open('input.txt','r')
n = int(input())
iList = list(map(int, input().split()))
iList.sort()
# print(iList)
minTime = 0
frontper = 0
if n==1:
    print(iList[0])
else:

    for i in range(n):
        minTime += frontper + iList[i]
        frontper += iList[i]
    print(minTime)