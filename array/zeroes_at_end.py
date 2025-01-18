"""def zeroes_at_end(arr):
    n = len(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            element = arr.pop(i)
            arr.insert(n, element)
    return arr

arr = [1,0,6,4,0,5]

result = zeroes_at_end(arr)
print(result)
"""
# -------------------------------------------------------------------

"""def zeroes_at_end(arr):
    temp = [0] * len(arr)  # temp is initialized with all zeroes [0,0,0,0,0,0]
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1
    return temp  # have to return temp not arr


arr = [1, 0, 6, 4, 0, 5]

result = zeroes_at_end(arr)
print(result)
"""


# working scenario

# If arr = [1, 0, 6, 4, 0, 5], temp starts as [0, 0, 0, 0, 0, 0].
# During the loop:
# temp[0] = 1 → temp = [1, 0, 0, 0, 0, 0]
# temp[1] = 6 → temp = [1, 6, 0, 0, 0, 0]
# temp[2] = 4 → temp = [1, 6, 4, 0, 0, 0]
# temp[3] = 5 → temp = [1, 6, 4, 5, 0, 0]


# ----------------------------------------------------------

def z_at_end(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr


arr = [1, 0, 6, 4, 0, 5]

result = z_at_end(arr)
print(result)
