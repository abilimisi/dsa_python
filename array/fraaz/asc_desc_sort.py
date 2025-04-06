# Function to check if the array is sorted forward, backward, or not sorted
def check_sorted(nums):
    is_ascending = True
    is_descending = True

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            is_ascending = False

        if nums[i] < nums[i + 1]:
            is_descending = False

    if is_ascending:
        return "Sorted in Forward Order"
    elif is_descending:
        return "Sorted in Backward Order"
    else:
        return "Not Sorted"


arr = [5,10,2]
print(check_sorted(arr))