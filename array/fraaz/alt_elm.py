def alternate_elements(arr):
    for i in range(0, len(arr), 2):
        print(arr[i], end=" ")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alternate_elements(arr)

# ---------------------------------------------------------
arrays = [1, 2, 3, 5, 6]
for i in range(len(arrays)):
    if i % 2 == 0:
        print(arrays[i], end=" ")

# ---------------------------------------------------------
array_s = [1, 2, 3, 5, 6]
print(array_s[::2])
