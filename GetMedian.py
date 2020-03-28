def median(arr1,arr2):
    if(len(arr1)!=1 and len(arr2)!=1):
        l1 = len(arr1)//2
        l2 = len(arr2)//2
        if(l1<l2):
            return median(arr1[l1:],arr2[:l2])
        elif(l2<l1):
            return median(arr1[:l1],arr2[l2:])
        else:
            return ((arr1[l1]+arr2[l2])//2)
    else:
            return ((arr1[l1]+arr2[l2])//2)

a=[1,2,3,4,5]
b=[4,5,6,7,8]
print('median: ',median(a,b))