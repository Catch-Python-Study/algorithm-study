import sys
import heapq as hq
sys.stdin = open('input.txt','r')

T = int(input())
heap = []

for i in range(T):
    x= int(input())
    if x!=0:
        hq.heappush(heap, (abs(x),x))
    else:
        try:
            print(hq.heappop(heap)[1])
        except:
            print(0)
