# def second_largest(arr):
#     arr.sort()
#
#     z = arr[-2]
#     if z != arr[0]:
#         return z
#     else:
#         return -1
#
# arr = [12,35,1,10,34]
#
# result = second_largest(arr)
# print(result)

def second_largest(arr):
    arr.sort()

    n = len(arr)

    for i in range(n-2,-1,-1):
        if arr[i] != arr[0]:
            return arr[i]
    return -1

arr = [12,12,12]

result = second_largest(arr)
print(result)