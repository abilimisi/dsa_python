def saperate_even_odd(arr):
    od = 0
    evn = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            evn += 1
        else:
            od += 1

    even = evn * [0]
    odd = od * [0]

    evn_count = 0
    odd_count = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even[evn_count] = arr[i]
            evn_count += 1
        else:
            odd[odd_count] = arr[i]
            odd_count += 1
    print(even, odd)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,23,44,37]
saperate_even_odd(arr)

#---------------------------------------------------------
# with append

arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,23,44,37]

even = []
odd = []

for i in range(len(arrays)):
    if arrays[i]%2 == 0:
        even.append(arrays[i])
    else:
        odd.append(arrays[i])
print(even,odd)