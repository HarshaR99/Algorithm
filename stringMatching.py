
def matchString(str1,str2) :
    n = len(str1)
    m = len(str2)
    if n < m :
        return -1
    for i in range(0,n-m) :
        j = 0
        while j < m and str1[i+j] == str2[j] :
            j += 1
        if j == m:
            return i
    return -1

str1 = input("Enter the text : ")
str2 = input("Enter the pattern : ")
pos = matchString(str1,str2)
if pos < 0 :
    print("Pattern not found")
else:
    print("Pattern found at "+str(pos))
