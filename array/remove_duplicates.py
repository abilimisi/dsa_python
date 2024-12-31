# time complexity 0(n)
# space complexity 0(n)

"""def remove_duplicates(elements):
    seen = set()
    idx = 0

    for num in range(len(elements)):
        if arr[num] not in seen:
            seen.add(arr[num])
            arr[idx] = arr[num]
            idx += 1
    return idx


arr = [1, 3, 3, 4, 5, 7, 7]
res = remove_duplicates(arr)
for i in range(res):
    print(arr[i], end=" ")"""


# ----------------------------------------------------------------

# time complexity 0(n)
# space complexity 0(1)
# recommended one
# below ex works only on sorted array
def rem_dup(arr):
    idx = 1  # start from 1 bcz we consider first element should be unique

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1
    return idx


arr = [1, 3, 3, 4, 5, 7, 7]
res = rem_dup(arr)
for i in range(res):
    print(arr[i], end=" ")  # OR
# print(arr[:res])

# -------------------------------------------------------

# time complexity 0(n)
# space complexity 0(1)

# arr1 = [1, 3, 3, 4, 5, 7, 7,3]
# for i in arr1:
#     if arr1.count(i) > 1:
#         arr1.remove(i)
# print(arr1)
