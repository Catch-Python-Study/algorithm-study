import sys
import heapq as hq
sys.stdin = open('input.txt','r')

T = int(input())
heap = []

for i in range(T):
    x = int(input())
    if x!=0:
        hq.heappush(heap, -x)
    else:
        try:
            print(-1*hq.heappop(heap))
        except:
            print(0)