def recurBin(array,key,first,last) : #function for recursive binary search
	mid = int((first+last-1)/2);
	if array[mid] == key :
		return 1;
	if mid == 0 :
		return 0;
	if key < a[mid] :
		return recurrBin(array,key,first,mid-1);
	else :
		return recurrBin(array,key,mid+1,last);

a = []
n = int(input("Enter number of elements : "));
for i in range(n) :
	ele = int(input("Element  :"));
	a.append(ele);
key = int(input("Enter key : "));
search = recurBin(a,key,0,len(a));
if search == 1 :
	print("Key is present")
else :
	print("Key is not present")
