def findSecondMaxElement(nums):
    maxElement = float('-inf')
    secondMaxElement = float('-inf')

    for num in nums:
        if num > maxElement:
            secondMaxElement = maxElement
            maxElement = num
        elif num > secondMaxElement and num != maxElement:
            secondMaxElement = num

    if secondMaxElement == float('-inf'):
        print(-1)
    else:
        print(secondMaxElement)

# Test case
nums = [1, 8, 4, 14, 19, 5]
findSecondMaxElement(nums)
