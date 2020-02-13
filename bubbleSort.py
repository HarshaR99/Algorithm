import time

n = int(input("Number of elements :"))
a = []
print('Enter the elements : ')
for i in range(n) :
	ele = int(input())
	a.append(ele)
start_time = time.time();
for i in range(n) :
	for j in range(n-i-1):
		if a[j] > a[j+1] :
			temp = a[j]
			a[j] = a[j+1]
			a[j+1] = temp; 
end_time = time.time()
total_time = end_time - start_time 
print("Sorted list is :")
for var in a :
	print(str(var))
print("Time taken for Algo is ",str(total_time));
