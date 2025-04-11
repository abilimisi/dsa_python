def max_element(nums):
    min = nums[0]
    for i in nums:
        if i<min:
            min = i

    return min

nums = [1,8,4,14,19,5,-1]
print(max_element(nums))