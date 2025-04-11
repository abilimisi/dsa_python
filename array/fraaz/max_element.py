def max_element(nums):
    max = nums[0]
    for i in nums:
        if i>max:
            max = i

    return max

nums = [1,8,4,14,19,5]
print(max_element(nums))