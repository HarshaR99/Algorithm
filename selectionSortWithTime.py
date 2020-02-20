# input : 5,6,1
# sorting :1,6,5
# output: 1,5,6
import random
import time

def selectionSort(arr):
	n = len(arr)
	for i in range(n-1):
		small = arr[i]
		pos = i
		for j in range(i+1,n):
			if small > arr[j]:
				small = arr[j]
				pos = j
		if i != pos :
			temp = arr[pos]
			arr[pos] = arr[i]
			arr[i] = temp

n = int(input("Enter the number of elements : "))
#arr = list(map(int,input().split()))
arr = []
for i in range(n):
	arr.append(int(random.random()*1000 + 1))
time_start = time.time()
selectionSort(arr)
time_end = time.time()
print("The sorted array is :\n"+str(arr))
print("Time taken is : "+str(time_end - time_start))
			
	

