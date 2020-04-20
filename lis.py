def lengthOfLIS(arr): 
    def _search(sub, val):
        l, h = 0, len(sub)-1
        while l <= h:
            mid = l + (h-l) // 2
            if sub[mid] < val:
                l = mid + 1
            elif sub[mid] > val:
                h = mid - 1
            else :
                return mid
        return l
    
    sub = []
    for val in arr:
        pos = _search(sub, val)
        if pos == len(sub):
            sub.append(val)
        else:
            sub[pos] = val
    return len(sub)
        
arr = list(map(int, input().split()))
print(lengthOfLIS(arr))
