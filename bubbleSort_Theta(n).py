def bubbleSort(arr):
    n = len(arr)
    flag = 0
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
        if flag == 0:
            break


print("Enter the elements of array : \n")
arr = list(map(int,input().split()))
bubbleSort(arr)
print("After sorting the array is : "+ str(arr))
