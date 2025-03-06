# def missingNumber(arr):
#     for i in range(1, len(arr)+1):
#         if i not in arr:
#             print(i)
# arr = [1,2,3,5]
# missingNumber(arr)

def mis_no(arr):
    for i in range(1,len(arr)+2):
        found = False

        for j in range(len(arr)):
            if arr[j] == i:
                found = True
                break

        if not found:
          return i

    else:
        return -1

arr = [1,2,3,4,6]
# arr = [1]
print(mis_no(arr))
