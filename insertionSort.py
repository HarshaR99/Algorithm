#program to perform insertion sort
import time

def insertionSort(arr,n):
	for i in range(n):
		key = arr[i]
		j = i - 1
		while (j >= 0) and (arr[j] > key):
			arr[j+1] = arr[j]
			j = j - 1
		arr[j+1] = key

	
print('Enter the array:\n')
arr = list(map(int,input().split()))
time_start = time.time()
insertionSort(arr,len(arr))
time_end = time.time()
print('Sorted array is :')
for i in arr:
	print(str(i))
print('Time taken to execute is : ',time_end-time_start)
