import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

#분할정복 (reference 有)
def solution(x,y,N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                solution(x,y,N//2)
                solution(x, y + N//2, N//2)
                solution(x + N//2, y, N//2)
                solution(x + N//2, y + N//2, N//2)

solution(0,0,N)
