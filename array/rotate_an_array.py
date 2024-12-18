#Time Complexity:O(n2)
# Space Complexity: O(1)

# def rotate_an_array(arr, n):
#     start = 0
#     end = len(arr) - 1
#     finish = n
#
#     while start < finish:
#         element = arr.pop(end)
#         arr.insert(0, element)
#         start += 1
#
#     return arr
#
#
# arr = [1, 2, 3, 4, 5, 6]
# n = 2
# res = rotate_an_array(arr, n)
# print(res)

def right_rotate(arr,d):
    d = d % len(arr)  # In case d > n
    rotated_array = arr[-d:] + arr[:-d]  #from 0 to -2
    return rotated_array


arr = [1, 2, 3, 4, 5, 6]
d = 2
res = right_rotate(arr,d)
print(res)

# Time Complexity:O(n)
# Space Complexity: O(n)