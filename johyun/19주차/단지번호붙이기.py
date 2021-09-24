# n= int(input()) #백준 제출용
import sys
n = int(sys.stdin.readline())
graph = []
visited=[[0]*n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int,input())))

#방향 확인용 좌표 dx와 dy
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,c):
    visited[x][y]=1   #방문여부 표시
    global nums       #아파트 단지 수를 세기 위함
    if graph[x][y]==1:
        nums+=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0<= ny < n:
            if visited[nx][ny] ==0 and graph[nx][ny]==1:
                dfs(nx,ny,c)

cnt=1       #아파트 단지 개수
numlist=[]  #아파트 단지별 갯수
nums=0      #아파트 수
for a in range(n):
    for b in range(n):
        if graph[a][b] ==1 and visited[a][b]==0:
            dfs(a,b,cnt)
            numlist.append(nums)
            nums=0
print(len(numlist))
for n in sorted(numlist):
    print(n)