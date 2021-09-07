import sys

sys.stdin = open("input.txt", "r")
n1, n2 =  map(int, sys.stdin.readline().split())
# print(n1,n2)
def solution():
    listt=[]
    for i in range(n1,n2+1):
        #n2가 3자리수일때
        if n2<1000:
            p100 = i//100
            p10 = (i%100)//10
            p1 = (i%100)%10
            result = (p100**3)+(p10**3)+(p1**3)
            if i==result:
                print(result , end='\t')

        #n2가 4자리수일때
        elif n2>999:
            p1000 = i//1000
            p100 = (i % 1000)//100
            p10 = (i % 100) // 10
            p1 = (i % 10)
            result = (p1000**4)+(p100**4)+(p10**4)+(p1**4)
            if i==result:
                print(result , end='\t')

solution()




