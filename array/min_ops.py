def min_ops(arr, k):
    min_element = min(arr)
    operations = 0

    for x in arr:
        diff = x - min_element
        if diff % k != 0:
            return -1

        operations += diff // k
    return operations


arr = [4, 7, 19, 16]
k = 3
print(min_ops(arr, k))
