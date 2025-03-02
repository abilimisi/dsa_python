def find_single(arr):

    n = len(arr)

    for i in range(n):
        count = 0

        for j in range(n):

            if arr[j] == arr[i]:
                count+=1

        if count == 1:
            print(arr[i])
arr = [1,2,3,4,1,3,4]
find_single(arr)