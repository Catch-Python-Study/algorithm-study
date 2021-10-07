import sys
from collections import deque

sys.stdin = open("input.txt", "r")
t = int(input())

for i in range(t):
    func = sys.stdin.readline().rstrip()  #함수
    n = int(input())  #배열 길이
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))  #배열
    print(arr)