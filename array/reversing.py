# class Solution:
#     def reverseArray(self,arr):
#         z = arr[::-1]
#         return z
#
#
# arr = [1, 4, 3, 2, 6, 5]
# res = Solution()
# print(res.reverseArray(arr))
#
#
# def reverseArray(arr):
#     for i in range(len(arr)-1,-1,-1):
#         print(arr[i],end=" ")
#
# arr = [1, 4, 3, 2, 6, 5]
# res = reverseArray(arr)



def reverseArray(arr):
    start = 0
    end = len(arr)-1

    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr

arr = [1, 4, 3, 2, 6, 5]
res = reverseArray(arr)
print(res)
