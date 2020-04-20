def partition(arr,low,high):
	pivot = arr[high-1]
	pindex = low
	for i in range(low,high-1):
		if arr[i] < pivot:
			arr[i], arr[pindex] = arr[pindex], arr[i]
			# print(True)
			pindex += 1
	arr[pindex],arr[high-1] = arr[high-1], arr[pindex]
	return pindex

def quicksort(arr,low,high):
	if low < high:
		pivot = partition(arr,low,high)
		quicksort(arr,low,pivot-1)
		quicksort(arr,pivot+1,high)


# driver code
arr = [2,1,7,6,8,5,3,4]
print('input array: ',arr)
quicksort(arr,0,len(arr))
print('sorterd array :',arr)
