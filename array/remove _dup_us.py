def rem_dup_un_sorted(arr):
    res = []
    for i in range(len(arr)):
        j = 0

        while j < i:
            if arr[i] == arr[j]:
                break
            j+=1

        if i == j:
            res.append(arr[i])

    return res
arr = [10,10,20,10,9,47,33,47]
res = rem_dup_un_sorted(arr)
for val in res:
    print(val,end = " ")