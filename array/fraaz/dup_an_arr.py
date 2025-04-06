def duplicate_an_array(arr):
    d_array = len(arr) * [0]

    for i in range(len(arr)):
        d_array[i] = arr[i]
    print(d_array)


arr = [1, 3, 5, 4, 6, 8, 2]
duplicate_an_array(arr)
