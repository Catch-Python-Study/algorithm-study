import numpy as np
testcase = int(input())

for test in range(testcase):
	n, k = map(int,input().split())
	land = np.array([])
	for i in range(n):
			arr = list(map(int, input().split()))
			land = np.append(land, arr, axis = 0)
	land = np.reshape(land,(n,n))

	new_land = np.zeros([n-(k-1),n-(k-1)])
	for i in range(n-(k-1)):
			for j in range(n-(k-1)):
					new_land[i,j] = np.sum(land[i:i+k,j:j+k])

	print(int(np.min(new_land)))