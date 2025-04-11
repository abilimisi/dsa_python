def find_target(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return True
    return False

nums = [2, 7, 11, 15]
target = 20

if find_target(nums, target):
    print("Found")
else:
    print("Not Found")
