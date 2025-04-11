def findSecondMinElement(nums):
    minElement = float('inf')
    secondMinElement = float('inf')

    for num in nums:
        if num < minElement:
            secondMinElement = minElement
            minElement = num
        elif num < secondMinElement and num != minElement:
            secondMinElement = num

    if secondMinElement == float('-inf'):
        print(-1)
    else:
        print(secondMinElement)

# Test case
nums = [1, 8, 4, 14, 19, 5,2]
findSecondMinElement(nums)
