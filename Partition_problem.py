def isSubsetSum (arr, n, sum): 
	if sum == 0: 
		return True
	if n == 0 and sum != 0: 
		return False
	if arr[n-1] > sum: 
		return isSubsetSum (arr, n-1, sum) 
	return isSubsetSum (arr, n-1, sum) or isSubsetSum (arr, n-1, sum-arr[n-1]) 
def findPartion (arr, n): 
	sum = 0
	for i in range(0, n): 
		sum += arr[i] 
	if sum % 2 != 0: 
		return False
	return isSubsetSum (arr, n, sum // 2) 


if __name__ == "__main__":
	arr = [int(i) for i in range(4)]

	n = len(arr) 
	if findPartion(arr, n) == True: 
		print ("Can be divided into two subsets of equal sum") 
	else: 
		print ("Can not be divided into two subsets of equal sum") 