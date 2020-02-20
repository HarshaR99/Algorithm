# input : 5,6,1
# sorting :1,6,5
# output: 1,5,6

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

print("Input the array :")
arr = list(map(int,input().split()))
selectionSort(arr)
print("The sorted array is :\n"+str(arr))
			
	

