import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
List = []

for _ in range(N):
    temp = list(map(int, input().split()))
    List.append(temp)

A = [[[0, 0], [0, 1], [0, 1], [0, 1]], [[0, 0], [1, 0], [1, 0], [1, 0]]]

B = [[0, 0], [0, 1], [1, 0], [0, -1]]

C = [[[0, 0], [1, 0], [1, 0], [0, 1]], 
[[0, 0], [0, 1], [0, 1], [-1, 0]], 
[[0, 0], [0, 1], [1, 0], [1, 0]], 
[[0, 0], [-1, 0], [0, 1], [0, 1]], 
[[0, 0], [1, 0], [1, 0], [0, 1]],
[[0, 0], [0, 1], [1, 0], [1, 0]],
[[0, 0], [0, 1], [0, 1], [1, 0]],
[[0, 0], [1, 0], [0, 1], [0, 1]]]

D = [[[0, 0], [1, 0], [0, 1], [1, 0]], [[0, 0], [0, 1], [-1, 0], [0, 1]], [[0, 0], [-1, 0], [0, 1], [-1, 0]], [[0, 0], [0, 1], [1, 0], [0, 1]]]

E = [[[0, 0], [0, 1], [-1, 0], [1, 1]], [[0, 0], [-1, 0], [0, 1], [-1, -1]], [[0, 0], [0, 1], [1, 0], [-1, 1]], [[0, 0], [0, 1], [1, 0], [-2, 0]]]

