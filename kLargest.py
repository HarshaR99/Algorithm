# function to get k largest elements of an array
def kLargestElements(a, k):
    n = len(a)
    for i in range(n - 1, n - k - 1, -1):
        pos = i
        for j in range(0, i):
            if a[j] > a[pos]:
                pos = j
        temp = a[i]
        a[i] = a[pos]
        a[pos] = temp
    for i in range(n-k,n):
        print(a[i])

a = [3, -5, 462, 5, 7, 2, 0]
kLargestElements(a, 3)



