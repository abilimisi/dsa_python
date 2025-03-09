def missing_repeating(arr):
    for i in range(1, len(arr)):
        if i not in arr:
            print(i)

    for i in range(len(arr) + 1):
        if arr.count(i) > 1:
            print(i)


arr = [1,2,4,5,5]
missing_repeating(arr)