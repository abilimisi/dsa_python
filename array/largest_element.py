def laergest_element(arr):

    num = arr[0]

    for i in arr:
        if i >= num:
            num = i
    return num

arr = [1,23,77,27,58]

result = laergest_element(arr)

print(result)