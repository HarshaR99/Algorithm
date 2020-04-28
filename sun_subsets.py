def subsetsum(array, num=21):
    if num < 0:
        return
    if len(array) == 0:
        if num == 0:
            yield []
        return
    for solution in subsetsum(array[1:], num):
        yield solution
    for solution in subsetsum(array[1:], num - array[0]):
        yield [array[0]] + solution


arr = list(map(int, input('Enter the array: ').split()))
n = int(input('Enter the sum:'))
print(*list(subsetsum(arr, n)))
