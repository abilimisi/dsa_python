def rev_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
    #or for i in range(len(arr) // 2):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


arr = [2, 4, 6, 8, 9]
res = rev_array(arr)
print(res)

val = [2, 4, 6, 8, 9]
for i in range(len(val) - 1, -1, -1):
    print(val[i], end=" ")
