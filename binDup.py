# 1,2,3,3,4,4,4,4,5,9  

def bin(a,key,first,last) :
	
	while first <= last :
		mid = int((first + last)/2);
		if a[mid] == key :
			return mid;
		elif a[mid] < key :
			first = mid + 1;
		else :
			last = mid -1;
	return -1;

def occur(a,mid,key) :  # helper function to find count,first occurence,last occurence
	first = -9
	mid1 = mid;
	mid2 = mid
	count = 0		
	while first != -1 :		
		first = bin(a,key,0,mid1-1);
		if first == -1 :
			break;
		mid1 = first;
		count += 1;
	if mid1 != -1 :
		print("First occurence is ",mid1);
	else :
		print("First occurence is ",mid);
	
	
	last = -9
	while last != -1 :
		last = bin(a,key,mid2+1,len(a));
		if last == -1 :
			break;
		mid2 = last
		count += 1;
	if mid2 != -1 :
		print("Last occurence is ",mid2);
	else :
		print("Last occurence is ",mid);
	if bin(a,key,0,len(a)) != -1 :	
		print("Number of occurences of key is ",count+1)
	else :
		print("Number of occurences of key is 0")
		

a = [1,2,3,3,4,4,4,4,5,9];  # array
occur(a,bin(a,4,0,len(a)),4);

