class Solution:
    def reverseArray(self,arr):

        for i in range(len(arr)-1,0,-1):
            for j in range(i):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

arr = [1, 4, 3, 2, 6, 5]
res = Solution()
print(res.reverseArray(arr))