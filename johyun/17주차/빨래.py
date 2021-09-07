##아직 미완입니다.
import sys
sys.stdin = open("input.txt", "r")
n,c =map(int,input().split())
color =str(input().split())
# dt = [sys.stdin.readline() for _ in range(n)]
no_and_color=[]
for i in range(c):
    no_and_color.append(input().split())

for data in no_and_color:
    if data[1]==color[0]:

