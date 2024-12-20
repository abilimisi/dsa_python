def reversing(arr, n):
    temp = [0] * n

    for i in range(n):
        temp[i] = arr[n - i - 1]
    return temp


arr = [1, 4, 3, 2, 6, 5]
n = len(arr)

print(reversing(arr, n))

# -------------------------------------------------------------


"""def reverseArray(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


arr = [1, 4, 3, 2, 6, 5]
res = reverseArray(arr)
print(res)

"""

# ------------------------------------------------------

"""class Solution:
    def reverseArray(self,arr):
        z = arr[::-1]
        return z


arr = [1, 4, 3, 2, 6, 5]
res = Solution()
print(res.reverseArray(arr))

"""

# -------------------------------------------------------------------


""" def reverseArray(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")


arr = [1, 4, 3, 2, 6, 5]
res = reverseArray(arr)

"""




