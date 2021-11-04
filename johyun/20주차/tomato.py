import sys
from collections import deque
# bfs사용
sys.stdin = open("input.txt", "r")
m,n,h = map(int,input().split())
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int,input().split())))
    # print(graph)
    for j in range(m):
        if graph[i][j]==1:
            queue.append([i,j])
    # print(queue)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<n and 0<=b<m and graph[a][b]==0:
                queue.append([a,b])
                graph[a][b] = graph[x][y]+1
bfs()
answ = 0
def aa():
    global answ
    for i in graph:
        for j in i:
            if j == 0:
                print(-1)
                return -1

        answ = max(answ, max(i))
    return answ- 1

aa()