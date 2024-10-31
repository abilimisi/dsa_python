class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = x[::-1]

        if reverse == x:
            return True
        else:
            return False
x = 121
result = Solution()
print(result.isPalindrome(str(x)))