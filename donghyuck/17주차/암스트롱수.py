import numpy as np
start, end = map(int, input().split())


for i in range(start, end+1):
    num = list(map(int, str(i)))
    num = np.array(num)
    if i == sum(num**3):
        print(i, end = ' ')