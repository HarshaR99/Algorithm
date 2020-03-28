def hasEvenNumOnes(num):
    count = 0
    while num>0:
        binDigit = num % 2
        num = num // 2
        if binDigit == 1:
            count = count + 1
    if count % 2 == 0:
        return True
    return False

def sumOfDigits(num):
    sum = 0
    while num > 0:
        sum = sum + (num % 10)
        num = num // 10
    return sum

# print(hasEvenNumOnes(1))
print('Enter elements of array\n')
arr = list(map(int,input().split()))
result = 0
for ele in arr:
    if hasEvenNumOnes(ele):
        result = result + sumOfDigits(ele)
print('Result : ',result)


