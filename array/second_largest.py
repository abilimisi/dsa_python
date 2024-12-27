# O(n*logn) Time and O(1) Space
def second_largest(arr):
    arr.sort()

    n = len(arr)

    for i in range(n - 2, -1, -1):
        if arr[i] != arr[0]:
            return arr[i]
    return -1


arr = [12, 37, 14, 48, 23]

result = second_largest(arr)
print(result)


# --------------------------------------------------------------------

# O(n) Time and O(1) Space
def sec_lar(arr):
    largest = -1
    s_largest = -1

    for i in arr:
        if i > largest:
            largest = i
    for j in arr:
        if j > s_largest and j != largest:
            s_largest = j
        return s_largest


arr = [12, 37, 14, 48, 23]
print(second_largest(arr))
