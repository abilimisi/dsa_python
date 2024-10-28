#bubble_sort - o(n2)


arr = [1, 2, 4, 2, 3, 5, 9, 6, 3, 6]

arr_len = len(arr)

for i in range(len(arr)-1, 0, -1):
    print(i)
    for j in range(i):
        if arr[j] >= arr[j+1]:
            swapped = True
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)
    
