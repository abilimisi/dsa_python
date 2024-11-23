# def distinct_element(arr):
#     s_arr = set(arr)
#     a_arr = list(s_arr)
#     a_arr.sort()
#
#     if len(a_arr) >= 3:
#         return a_arr[-3:]
#     return a_arr
#
#
# arr = [10, 4, 3, 50, 23, 90, 50]
#
# result = distinct_element(arr)
# print(result[::-1])


def distinct_element(arr):
    arr_size = len(arr)
    if arr_size < 3:
        print("invalid input")
        return

    third = first = second = float('-inf')

    for i in range(arr_size):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]

        elif arr[i] > third and arr[i] != first and arr[i] != second:
            third = arr[i]

    print("Three largest elements are : ", first, second, third)


arr = [12, 13, 1, 10, 34, 11, 34]
distinct_element(arr)
