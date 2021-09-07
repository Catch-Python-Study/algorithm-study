import sys
import sys
sys.stdin = open("./input.txt", "r")
k=int(sys.stdin.readline())
print(k)


def solution(k):
    q=2
    while q <= k:
        if k%q == 0:
            k = k/q
            print(q , end=' ')
        else:
            q+=1

solution(k)