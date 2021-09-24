# t = int(input())  #백준 제출용

import sys
sys.stdin = open("input.txt", "r")
cases =int(input()) #테스트케이스 수

for i in range(cases):
    n = int(input()) #의상 수
    weardict = {}
    for j in range(n):
        wear = list(input().split())
        print(wear)
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1 # 각 종류마다 항목의 개수
    print(weardict)

    for k in weardict:
        cnt *= (len(weardict[k])+1) #해당 항목을 하나도 걸치지 않는 경우 더해주기
    print(cnt-1) #알몸인 경우 빼주기
